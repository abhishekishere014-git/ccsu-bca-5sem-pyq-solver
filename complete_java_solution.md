## Section - A (Very Short Answer Questions — 3 Marks Each, All 5 Mandatory)

### Q1. Why is Java called a Machine Independent language?
**Answer:**
Java source code (`.java`) is compiled by `javac` into an intermediate, architecture-neutral binary bytecode (`.class`). This bytecode runs on any device containing a platform-specific **Java Virtual Machine (JVM)**, fulfilling the motto *"Write Once, Run Anywhere"* (WORA).

---

### Q2. Explain the functionality and architecture of JVM.
**Answer:**
The JVM (Java Virtual Machine) consists of three primary subsystems:
1. **Class Loader:** Loads, links, and initializes binary bytecode into memory.
2. **Memory Data Areas:** Method Area (class structures), Heap (objects), Stack (method call frames), PC Registers, and Native Method Stack.
3. **Execution Engine:** Interprets bytecode, compiles hotspots via Just-In-Time (JIT) compiler to native instructions, and manages Garbage Collection.

---

### Q3. Explain the 'super' keyword in Java with examples.
**Answer:**
The `super` reference variable refers directly to the immediate parent class:
1. `super.variableName;` — accesses hidden superclass member variables.
2. `super.methodName();` — invokes overridden superclass methods.
3. `super();` or `super(args);` — invokes parent constructor (must be the very first statement in subclass constructor).

---

### Q4. Differentiate between Process-based and Thread-based Multitasking.
**Answer:**
- **Process-based:** Multiple independent applications run simultaneously. Each process has isolated private memory. Inter-process communication is heavy.
- **Thread-based:** Multiple concurrent execution paths within the same single application. Threads share identical heap memory and resources with minimal CPU context-switch overhead.

---

### Q5. Explain Anchor tag (`<a>`) and Table tag (`<table>`) in HTML.
**Answer:**
- **Anchor Tag:** `<a href="page.html" target="_blank">Link</a>` creates navigable hyperlinks.
- **Table Tag:** `<table border="1">` organizes tabular information using rows (`<tr>`), table headers (`<th>`), and data cells (`<td>`).

---

## Section - B (Short Answer Questions — 7.5 Marks Each, Attempt Any Two)

### Q6. What is an Exception? How do you handle multiple exceptions and use the finally block?
**Answer:**
An Exception disrupts normal application flow. Handled via `try-catch-finally`:
```java
try {
    int[] nums = {10, 20};
    int res = nums[1] / Integer.parseInt("0");
} catch (ArithmeticException e) {
    System.out.println("Math error: " + e.getMessage());
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("Array index invalid: " + e.getMessage());
} catch (Exception e) {
    System.out.println("Generic error: " + e.getMessage());
} finally {
    System.out.println("Always executed: cleaning resources.");
}
```

---

### Q7. Explain Applet Life Cycle and write a program to display an image.
**Answer:**
**Life Cycle Methods:** `init()` -> `start()` -> `paint(Graphics g)` -> `stop()` -> `destroy()`.
**Code Example:**
```java
import java.applet.Applet;
import java.awt.Graphics;
import java.awt.Image;

public class ImageApplet extends Applet {
    Image img;
    public void init() {
        img = getImage(getDocumentBase(), "banner.jpg");
    }
    public void paint(Graphics g) {
        g.drawImage(img, 20, 20, this);
        g.drawString("CCSU BCA 5th Sem Applet Display", 20, 220);
    }
}
```

---

### Q8. Explain Threads and two ways to create Threads in Java.
**Answer:**
1. **Extending `Thread` Class:**
   ```java
   class Worker extends Thread {
       public void run() { System.out.println("Thread running."); }
   }
   new Worker().start();
   ```
2. **Implementing `Runnable` Interface:**
   ```java
   class Task implements Runnable {
       public void run() { System.out.println("Runnable running."); }
   }
   new Thread(new Task()).start();
   ```

---

## Section - C (Long Answer Questions — 15 Marks Each, Attempt Any Three)

### Q9. Illustrate Inheritance. Why is multiple inheritance not possible in Java? How is it implemented via Interfaces?
**Answer:**
Inheritance allows a subclass to acquire properties of a parent class.
**Diamond Problem:** If Class C inherits from both Class A and Class B which both implement `display()`, Class C suffers ambiguity.
**Resolution using Interfaces:**
```java
interface Printable { void print(); }
interface Showable { void show(); }

class Report implements Printable, Showable {
    public void print() { System.out.println("Printing report."); }
    public void show() { System.out.println("Showing report."); }
}
```

---

### Q10. What is JDBC? Explain types of JDBC drivers. Write a program to insert and select records using PreparedStatement.
**Answer:**
JDBC (Java Database Connectivity) allows Java programs to execute SQL commands:
- **Type-1:** JDBC-ODBC bridge (obsolete)
- **Type-2:** Native-API driver
- **Type-3:** Network-protocol middleware driver
- **Type-4:** Thin driver (pure Java direct socket connection)

**Code:**
```java
import java.sql.*;

public class JdbcDemo {
    public static void main(String[] args) throws Exception {
        Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/college", "root", "pass");
        
        // Insert
        PreparedStatement psInsert = con.prepareStatement("INSERT INTO student VALUES (?, ?)");
        psInsert.setInt(1, 101);
        psInsert.setString(2, "Rahul");
        psInsert.executeUpdate();
        
        // Select
        PreparedStatement psSelect = con.prepareStatement("SELECT * FROM student");
        ResultSet rs = psSelect.executeQuery();
        while(rs.next()) {
            System.out.println(rs.getInt(1) + " : " + rs.getString(2));
        }
        con.close();
    }
}
```

---

### Q11. Explain Servlets and their Life Cycle. Compare Servlets and JSP.
**Answer:**
**Servlet Life Cycle (`javax.servlet.Servlet`):**
1. `init(ServletConfig config)`: Initialized once.
2. `service(ServletRequest req, ServletResponse res)`: Dispatches to `doGet()`/`doPost()`.
3. `destroy()`: Cleans up before unloading.

**Comparison:**
- **Servlets:** Pure Java with embedded HTML in print statements; best for controllers.
- **JSP:** HTML with embedded Java tags (`<% ... %>`); best for views.

---

### Q12. Explain TCP/IP Socket Programming (ServerSocket and Socket).
**Answer:**
- **Server:** `ServerSocket ss = new ServerSocket(8080); Socket s = ss.accept();`
- **Client:** `Socket s = new Socket("localhost", 8080);`
- Data exchanged via `InputStream`, `OutputStream`, `BufferedReader`, and `PrintWriter`.

---

### Q13. Discuss Layout Managers in Java AWT/Swing (FlowLayout, BorderLayout, GridLayout, CardLayout, GridBagLayout).
**Answer:**
1. **FlowLayout:** Aligns components in a row, wrapping when space ends.
2. **BorderLayout:** 5 regions: North, South, East, West, Center.
3. **GridLayout:** Arranges components in equal rectangular grid cells.
4. **CardLayout:** Shows one card/component at a time in a stack.
5. **GridBagLayout:** Dynamic, flexible grid with constraint parameters.
