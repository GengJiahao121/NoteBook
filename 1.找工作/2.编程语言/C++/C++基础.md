## C++ 基础

### C++ 三大特性

访问权限

C++通过 public、protected、private 三个关键字来控制成员变量和成员函数的访问权限，它们分别表示公有的、 受保护的、私有的，被称为成员访问限定符。

在**类的内部**(定义类的代码内部)，无论成员被声明为 public、protected 还是 private，**都是可以互相访问**的，没 有访问权限的限制。

在类的外部(定义类的代码之外)，只能通过对象访问成员，并且**通过对象只能访问 public 属性的成员**，不能访问 private、protected 属性的成员。

无论共有继承、私有和保护继承，**私有成员不能被“派生类”访问**，基类中的共有和保护成员能被“派生类”访问。

对于**共有继承**，只有**基类中的共有成员能被“派生类对象”访问**，保护和私有成员不能被“派生类对象”访问。对于私
有和保护继承，基类中的所有成员不能被“派生类对象”访问。

1. 继承

定义:

让某种类型对象获得另一个类型对象的属性和方法

功能:

它可以使用现有类的所有功能，并在无需重新编写原来的类的情况下对这些功能进行扩展

常见的继承有三种方式:

1、实现继承:指使用基类的属性和方法而无需额外编码的能力

```
#include <iostream>

// 基类
class Shape {
public:
    void draw() {
        std::cout << "Drawing a shape." << std::endl;
    }
};

// 派生类
class Circle : public Shape {
public:
    // 这里不需要重新实现 draw()，直接继承自基类
    double calculateArea() {
        return 3.14 * radius * radius;
    }

private:
    double radius;
};

int main() {
    Circle circle;
    circle.draw();  // 直接使用基类的方法
    double area = circle.calculateArea();
    std::cout << "Area of the circle: " << area << std::endl;

    return 0;
}
```

2、接口继承:指仅使用属性和方法的名称、但是子类必须提供实现的能力

```
// 接口定义
interface Playable {
    void play();
}

// 实现接口的类
class MusicPlayer implements Playable {
    @Override
    public void play() {
        System.out.println("Playing music.");
    }

    // 其他类必须提供 play() 方法的具体实现
}

public class Main {
    public static void main(String[] args) {
        MusicPlayer player = new MusicPlayer();
        player.play();
    }
}

```

3、可视继承:指子窗体(类)使用基窗体(类)的外观和实现代码的能力

QT中用的比较多

例如:

将人定义为一个抽象类，拥有姓名、性别、年龄等公共属性，吃饭、睡觉等公共方法，在定义一个具体的人时，就
可以继承这个抽象类，既保留了公共属性和方法，也可以在此基础上扩展跳舞、唱歌等特有方法。

2. 封装

定义:

数据和代码捆绑在一起，避免外界干扰和不确定性访问;

功能:

把客观事物封装成抽象的类，并且类可以把自己的数据和方法只让可信的类或者对象操作，对不可信的进行信息隐藏，例如:将公共的数据或方法使用public修饰，而不希望被访问的数据或方法采用private修饰。

3. 多态

定义:

同一事物表现出不同事物的能力，即向不同对象发送同一消息，不同的对象在接收时会产生不同的行为(**重载实现
编译时多态，虚函数实现运行时多态**)

功能:

多态性是允许你将父对象设置成为和一个或更多的他的子对象相等的技术，赋值之后，父对象就可以根据当前赋值 给它的子对象的特性以不同的方式运作;

简单一句话:允许将子类类型的指针赋值给父类类型的指针。

实现多态有两种方式

1. 覆盖(override): 是指子类重新定义父类的虚函数的做法.通过在基类中声明虚函数，并在派生类中覆盖它，可以在运行时通过基类指针或引用调用相应的派生类函数。

**虚函数和虚函数表（Virtual Functions and Virtual Function Table）**

```
#include <iostream>

class Shape {
public:
    virtual void draw() const {
        std::cout << "Drawing a shape." << std::endl;
    }
};

class Circle : public Shape {
public:
    void draw() const override {
        std::cout << "Drawing a circle." << std::endl;
    }
};

class Square : public Shape {
public:
    void draw() const override {
        std::cout << "Drawing a square." << std::endl;
    }
};

int main() {
    Shape* shape1 = new Circle();
    Shape* shape2 = new Square();

    shape1->draw();  // 输出 "Drawing a circle."
    shape2->draw();  // 输出 "Drawing a square."

    delete shape1;
    delete shape2;

    return 0;
}

```
**纯虚函数和抽象类（Pure Virtual Functions and Abstract Classes）**

```
#include <iostream>

class Shape {
public:
    virtual void draw() const = 0;  // 纯虚函数
};

class Circle : public Shape {
public:
    void draw() const override {
        std::cout << "Drawing a circle." << std::endl;
    }
};

class Square : public Shape {
public:
    void draw() const override {
        std::cout << "Drawing a square." << std::endl;
    }
};

int main() {
    // Shape* shape = new Shape();  // 错误，抽象类不能实例化

    Shape* shape1 = new Circle();
    Shape* shape2 = new Square();

    shape1->draw();  // 输出 "Drawing a circle."
    shape2->draw();  // 输出 "Drawing a square."

    delete shape1;
    delete shape2;

    return 0;
}

```

我的疑惑：

1、 virtual

在C++中，virtual 关键字用于声明虚函数。虚函数是一种在**运行时**动态绑定的机制，允许基类的指针或引用在运行时调用派生类的函数。

2、 const的不同位置分别代表的作用

    1. 修饰指针：

    const int* ptr; // 这表示指针 ptr 指向的值是常量，不能通过 ptr 修改所指向的值，但可以指向其他地方。

    2. 修饰指针所指向的值：

    int const* ptr; // 与上例相同，ptr 指向的值是常量，不能通过 ptr 修改所指向的值。

    3. 修饰引用

    const int& ref = someValue; // 这表示 ref 是对 someValue 的常量引用，不能通过 ref 修改 someValue 的值。

    4. const修饰成员函数：

    ```
    class MyClass {
        public:
            void someFunction() const {
                // 不能修改成员变量
            }
    };
    ```

    在成员函数后加上 const 表示该成员函数是一个常量成员函数，不能修改类的成员变量。它被设计为不会修改类的状态。

    5. 修饰对象

    const MyClass myObject; // 这表示 myObject 是一个常量对象，不能通过 myObject 修改其成员变量。

    6. const修饰成员函数的返回值：

    ```
    class MyClass {
    public:
        int getValue() const {
            return someValue;
        }
    };

    ```
    在成员函数声明和定义中的 const 表示该函数不会修改类的成员变量，**并且可以在常量对象上调用。**

    常量对象只能调用常量方法吗？是的， 但 常量方法可以被常量对象和非常量对象调用 

2. 重载(overload): 是指允许存在多个同名函数，而这些函数的参数表不同(或许参数个数不同，或许参数类型
不同，或许两者都不同)

函数重载（Function Overloading）

```
#include <iostream>

void print(int x) {
    std::cout << "Printing integer: " << x << std::endl;
}

void print(double y) {
    std::cout << "Printing double: " << y << std::endl;
}

int main() {
    print(5);
    print(3.14);

    return 0;
}

```

运算符重载（Operator Overloading）：可以通过运算符重载为用户定义的数据类型定义自定义的行为。

```
#include <iostream>

class Complex {
public:
    Complex(double real, double imag) : real(real), imag(imag) {}

    Complex operator+(const Complex& other) const {
        return Complex(real + other.real, imag + other.imag);
    }

    void display() const {
        std::cout << real << " + " << imag << "i" << std::endl;
    }

private:
    double real;
    double imag;
};

int main() {
    Complex c1(2.0, 3.0);
    Complex c2(1.0, 4.0);

    Complex result = c1 + c2;
    result.display();

    return 0;
}

```

例如:

基类是一个抽象对象——人，那学生、运动员也是人，而使用这个抽象对象既可以表示学生、也可以表示运动员。


### STL常用容器

STL 容器是 C++ 标准库提供的一组通用的模板类，用于存储和操作数据。它包括了各种容器类型，如向量（vector）、列表（list）、映射（map）等。



### c++数据类型

基本数据类型：整数、浮点数、字符和布尔类型

复合数据类型：是由基本数据类型和其他复合数据类型组合而成的用户自定义数据类型。
