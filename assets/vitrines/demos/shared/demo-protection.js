/**
 * Page de demonstration vitrine : bandeau + message console.
 * L'HTML servi au navigateur reste toujours recuperable (DevTools, reseau) :
 * la protection reelle = contrat / livraison archive apres achat + eventuel hebergement restreint.
 */
(function () {
  var doc = document.documentElement;
  doc.classList.add("dc-demo-page");

  var path = location.pathname || "";
  var m = path.match(/\/vitrines\/([^/]+)\/demo\//);
  var slug = m ? m[1] : "";
  var detailHref = slug ? "/vitrines/" + slug + "/" : "/vitrines/";

  var strip = document.createElement("div");
  strip.id = "dc-demo-strip";
  strip.setAttribute("role", "status");
  strip.setAttribute("aria-live", "polite");

  var muted = document.createElement("span");
  muted.className = "dc-demo-strip-muted";
  muted.textContent =
    "Démo en ligne uniquement — le code source et les fichiers sont réservés aux acheteurs. " +
    "Toute réutilisation ou republication sans accord est interdite.";

  var link = document.createElement("a");
  link.href = detailHref;
  link.textContent = "Fiche vitrine & achat";

  strip.appendChild(muted);
  strip.appendChild(link);

  function mount() {
    document.body.appendChild(strip);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mount, { once: true });
  } else {
    mount();
  }

  if (typeof console !== "undefined" && console.info) {
    console.info(
      "[DanielCraft] Maquette de démonstration — sources non libres. " +
        "Pour une version exploitable : achat sur la fiche vitrine."
    );
  }

  document.addEventListener(
    "dragstart",
    function (e) {
      if (e.target && e.target.closest && e.target.closest("img, picture, a[download]")) {
        e.preventDefault();
      }
    },
    { capture: true }
  );
})();
