# Classes et objets

```cpp
class Compte {
private:
    double solde;
public:
    Compte(double s) : solde(s) {}
    void depot(double m) { solde += m; }
    double lire() const { return solde; }
};
```
