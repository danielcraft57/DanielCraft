# Pointeurs et memoire

```cpp
int x = 42;
int* p = &x;
std::cout << *p << "\n";
```

Allocation dynamique :

```cpp
int* tab = new int[10];
delete[] tab;
```

> **Piege** - Oublier `delete` provoque des fuites memoire.
