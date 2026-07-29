# Gestion d'erreurs

```cpp
try {
    throw std::runtime_error("Probleme");
} catch (const std::exception& e) {
    std::cout << e.what() << "\n";
}
```

En C moderne, on combine exceptions, validation d'entrees et assertions.
