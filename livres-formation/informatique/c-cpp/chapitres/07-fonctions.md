# Fonctions

```cpp
int addition(int a, int b) {
    return a + b;
}
```

Passe par reference pour eviter des copies :

```cpp
void afficher(const std::string& nom) {
    std::cout << nom << "\n";
}
```
