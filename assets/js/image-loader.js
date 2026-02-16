/* ========================================
   IMAGE LOADER - WebP avec fallback et cache
   ======================================== */

/** URL de l'image de remplacement en cas d'echec de chargement */
const PLACEHOLDER_IMAGE_URL = 'assets/images/projets/placeholder.svg';

/**
 * Gestionnaire de chargement d'images optimisé avec support WebP et cache navigateur
 */

class ImageLoader {
    constructor() {
        this.webpSupported = null;
        this.imageCache = new Map();
        this.placeholderUrl = PLACEHOLDER_IMAGE_URL;
        this.preloadQueue = [];
        this.maxCacheSize = 50; // Nombre max d'images en cache mémoire
        this.dbName = 'danielcraft-image-cache';
        this.dbVersion = 1;
        this.db = null;
        this.checkWebPSupport();
        this.initIndexedDB();
    }

    /**
     * Initialise IndexedDB pour le cache persistant
     */
    async initIndexedDB() {
        if (!('indexedDB' in window)) {
            console.warn('IndexedDB non supporté, utilisation du cache mémoire uniquement');
            return;
        }

        return new Promise((resolve, reject) => {
            const request = indexedDB.open(this.dbName, this.dbVersion);

            request.onerror = () => {
                console.warn('Impossible d\'ouvrir IndexedDB, utilisation du cache mémoire uniquement');
                resolve(null);
            };

            request.onsuccess = () => {
                this.db = request.result;
                resolve(this.db);
            };

            request.onupgradeneeded = (event) => {
                const db = event.target.result;
                if (!db.objectStoreNames.contains('images')) {
                    db.createObjectStore('images', { keyPath: 'url' });
                }
            };
        });
    }

    /**
     * Récupère une image depuis le cache IndexedDB
     * @param {string} imageUrl - URL de l'image
     * @returns {Promise<string|null>} URL WebP ou null si non trouvé
     */
    async getFromIndexedDBCache(imageUrl) {
        if (!this.db) return null;

        return new Promise((resolve) => {
            const transaction = this.db.transaction(['images'], 'readonly');
            const store = transaction.objectStore('images');
            const request = store.get(imageUrl);

            request.onsuccess = () => {
                const result = request.result;
                if (result && result.webpUrl) {
                    // Vérifie que l'image existe toujours
                    const testImg = new Image();
                    testImg.onload = () => resolve(result.webpUrl);
                    testImg.onerror = () => resolve(null);
                    testImg.src = result.webpUrl;
                } else {
                    resolve(null);
                }
            };

            request.onerror = () => resolve(null);
        });
    }

    /**
     * Met en cache une image dans IndexedDB
     * @param {string} imageUrl - URL originale
     * @param {string} webpUrl - URL WebP
     */
    async saveToIndexedDBCache(imageUrl, webpUrl) {
        if (!this.db) return;

        try {
            const transaction = this.db.transaction(['images'], 'readwrite');
            const store = transaction.objectStore('images');
            await store.put({
                url: imageUrl,
                webpUrl: webpUrl,
                timestamp: Date.now()
            });
        } catch (error) {
            console.warn('Erreur lors de la sauvegarde dans IndexedDB:', error);
        }
    }

    /**
     * Vérifie si le navigateur supporte WebP
     * @returns {Promise<boolean>}
     */
    checkWebPSupport() {
        if (this.webpSupported !== null) {
            return Promise.resolve(this.webpSupported);
        }

        return new Promise((resolve) => {
            const webP = new Image();
            webP.onload = webP.onerror = () => {
                this.webpSupported = webP.height === 2;
                resolve(this.webpSupported);
            };
            webP.src = 'data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA';
        });
    }

    /**
     * Convertit une URL d'image en version WebP si disponible
     * @param {string} imageUrl - URL de l'image originale
     * @returns {Promise<string>} URL WebP ou originale
     */
    async getWebPUrl(imageUrl) {
        if (!imageUrl) return imageUrl;
        
        const supportsWebP = await this.checkWebPSupport();
        if (!supportsWebP) return imageUrl;

        // Vérifie d'abord le cache IndexedDB
        const cachedWebp = await this.getFromIndexedDBCache(imageUrl);
        if (cachedWebp) {
            return cachedWebp;
        }

        // Vérifie le cache mémoire
        if (this.imageCache.has(imageUrl)) {
            return this.imageCache.get(imageUrl);
        }

        // Si l'URL se termine par .jpg, .jpeg ou .png, on essaie .webp
        const webpUrl = imageUrl.replace(/\.(jpg|jpeg|png)$/i, '.webp');
        
        // Vérifie si le fichier WebP existe (on essaie de le charger)
        return new Promise((resolve) => {
            const testImg = new Image();
            testImg.onload = () => {
                // Met en cache
                this.imageCache.set(imageUrl, webpUrl);
                this.saveToIndexedDBCache(imageUrl, webpUrl);
                resolve(webpUrl);
            };
            testImg.onerror = () => {
                // Fallback sur l'original et met en cache
                this.imageCache.set(imageUrl, imageUrl);
                this.saveToIndexedDBCache(imageUrl, imageUrl);
                resolve(imageUrl);
            };
            testImg.src = webpUrl;
        });
    }

    /**
     * Charge une image avec cache et preload
     * @param {HTMLImageElement} imgElement - Élément img à charger
     * @param {string} imageUrl - URL de l'image
     * @param {Object} options - Options de chargement
     * @returns {Promise<void>}
     */
    async loadImage(imgElement, imageUrl, options = {}) {
        if (!imgElement || !imageUrl) return;

        const {
            useWebP = true,
            useCache = true,
            priority = 'auto',
            onLoad = null,
            onError = null
        } = options;

        // Vérifie le cache mémoire
        if (useCache && this.imageCache.has(imageUrl)) {
            const cachedUrl = this.imageCache.get(imageUrl);
            imgElement.src = cachedUrl;
            if (onLoad) imgElement.addEventListener('load', onLoad, { once: true });
            return;
        }

        // Détermine l'URL à utiliser (WebP ou original)
        const finalUrl = useWebP ? await this.getWebPUrl(imageUrl) : imageUrl;

        // Preload si priorité élevée
        if (priority === 'high') {
            this.preloadImage(finalUrl);
        }

        // Charge l'image
        return new Promise((resolve, reject) => {
            imgElement.onload = () => {
                // Met en cache
                if (useCache) {
                    if (this.imageCache.size >= this.maxCacheSize) {
                        // Supprime le premier élément (FIFO)
                        const firstKey = this.imageCache.keys().next().value;
                        this.imageCache.delete(firstKey);
                    }
                    this.imageCache.set(imageUrl, finalUrl);
                }
                
                imgElement.classList.add('loaded');
                if (onLoad) onLoad();
                resolve();
            };

            imgElement.onerror = () => {
                const clearPictureWebPSource = () => {
                    const picture = imgElement.closest('picture');
                    if (picture) {
                        const source = picture.querySelector('source[type="image/webp"]');
                        if (source) source.removeAttribute('srcset');
                    }
                };
                if (useWebP && finalUrl !== imageUrl) {
                    imgElement.src = imageUrl;
                    imgElement.onerror = () => {
                        clearPictureWebPSource();
                        imgElement.onload = () => imgElement.classList.add('loaded');
                        imgElement.src = this.placeholderUrl;
                        imgElement.classList.add('image-missing');
                        if (onError) onError();
                        resolve();
                    };
                } else {
                    clearPictureWebPSource();
                    imgElement.onload = () => imgElement.classList.add('loaded');
                    imgElement.src = this.placeholderUrl;
                    imgElement.classList.add('image-missing');
                    if (onError) onError();
                    resolve();
                }
            };

            imgElement.src = finalUrl;
        });
    }

    /**
     * Preload une image pour améliorer les performances
     * @param {string} imageUrl - URL de l'image à preload
     */
    preloadImage(imageUrl) {
        if (this.preloadQueue.includes(imageUrl)) return;
        
        this.preloadQueue.push(imageUrl);
        const link = document.createElement('link');
        link.rel = 'preload';
        link.as = 'image';
        link.href = imageUrl;
        document.head.appendChild(link);
    }

    /**
     * Charge plusieurs images avec lazy loading et étalement
     * @param {NodeList|Array} imgElements - Liste des éléments img
     * @param {Object} options - Options de chargement
     */
    async loadImagesStaggered(imgElements, options = {}) {
        const {
            staggerMs = 80,
            eagerCount = 3,
            useWebP = true,
            useCache = true
        } = options;

        const images = Array.from(imgElements);
        
        for (let i = 0; i < images.length; i++) {
            const img = images[i];
            
            // Si l'image est dans un picture, on utilise le source WebP si disponible (evite srcset="null")
            const picture = img.closest('picture');
            if (picture && useWebP) {
                const source = picture.querySelector('source[data-src]');
                if (source) {
                    const webpSrc = source.getAttribute('data-src');
                    const delay = i < eagerCount ? 0 : (i - eagerCount) * staggerMs;
                    setTimeout(() => {
                        if (webpSrc) {
                            source.srcset = webpSrc;
                            source.removeAttribute('data-src');
                        }
                    }, delay);
                }
            }
            
            const dataSrc = img.getAttribute('data-src');
            if (!dataSrc) continue;

            const delay = i < eagerCount ? 0 : (i - eagerCount) * staggerMs;
            const priority = i < eagerCount ? 'high' : 'auto';

            setTimeout(async () => {
                try {
                    await this.loadImage(img, dataSrc, {
                        useWebP,
                        useCache,
                        priority,
                        onLoad: () => img.removeAttribute('data-src')
                    });
                } catch (error) {
                    console.warn('Erreur lors du chargement de l\'image:', error);
                }
            }, delay);
        }
    }

    /**
     * Crée un élément picture avec source WebP et fallback
     * @param {string} imageUrl - URL de l'image originale
     * @param {string} alt - Texte alternatif
     * @param {Object} options - Options supplémentaires
     * @returns {HTMLElement} Élément picture
     */
    createPictureElement(imageUrl, alt = '', options = {}) {
        const {
            loading = 'lazy',
            decoding = 'async',
            className = '',
            sizes = null,
            srcset = null
        } = options;

        const picture = document.createElement('picture');
        const webpSource = document.createElement('source');
        webpSource.type = 'image/webp';
        webpSource.srcset = srcset || imageUrl.replace(/\.(jpg|jpeg|png)$/i, '.webp');
        if (sizes) webpSource.sizes = sizes;

        const img = document.createElement('img');
        img.src = imageUrl;
        img.alt = alt;
        img.loading = loading;
        img.decoding = decoding;
        if (className) img.className = className;

        picture.appendChild(webpSource);
        picture.appendChild(img);

        return picture;
    }

    /**
     * Nettoie le cache mémoire
     */
    clearCache() {
        this.imageCache.clear();
    }
}

// Instance globale
const imageLoader = new ImageLoader();

// Export pour utilisation globale
window.ImageLoader = ImageLoader;
window.imageLoader = imageLoader;
