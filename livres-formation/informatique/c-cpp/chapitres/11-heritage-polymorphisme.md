# Heritage et polymorphisme

```cpp
class Animal {
public:
    virtual void parler() const { std::cout << "..." << "\n"; }
    virtual ~Animal() = default;
};

class Chien : public Animal {
public:
    void parler() const override { std::cout << "Wouf" << "\n"; }
};
```
