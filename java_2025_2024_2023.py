import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from java_builder_base import generate_java_pdf

# ==============================================================================
# YEAR 2025 (December 2025)
# ==============================================================================
YEAR_2025_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>What is the difference between Process-based and Thread-based multitasking in Java?</div>
    <div class="ans-body">
        <strong>Comparison:</strong>
        <table class="grid-table">
            <thead><tr><th>Feature</th><th>Process-Based Multitasking</th><th>Thread-Based Multitasking</th></tr></thead>
            <tbody>
                <tr><td>Granularity</td><td>Heavyweight; each process has its own separate address space.</td><td>Lightweight; threads share the same address space in a single process.</td></tr>
                <tr><td>Context Switching</td><td>High overhead; managed by operating system kernel.</td><td>Low overhead; switches quickly within the JVM.</td></tr>
                <tr><td>Communication</td><td>Requires Inter-Process Communication (IPC, sockets, pipes).</td><td>Direct shared memory, wait(), notify(), synchronized blocks.</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Explain the 'super' keyword in Java with usages.</div>
    <div class="ans-body">
        <strong>Usage of 'super':</strong> A reference variable used in a subclass to refer directly to its immediate parent class object:
        <ol>
            <li><strong>Invoke Parent Constructor:</strong> <code>super(args);</code> &mdash; must be the first line in subclass constructor.</li>
            <li><strong>Access Parent Variables:</strong> <code>super.variableName</code> &mdash; accesses shadowed parent instance fields.</li>
            <li><strong>Call Parent Methods:</strong> <code>super.methodName()</code> &mdash; invokes overridden parent class methods.</li>
        </ol>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>What is Bytecode in Java? Why does it enable platform independence?</div>
    <div class="ans-body">
        <strong>Explanation:</strong> Java source code (<code>.java</code>) is compiled by <code>javac</code> into an intermediate machine-independent format called <strong>Bytecode</strong> (stored in <code>.class</code> files). Any platform equipped with a standard Java Virtual Machine (JVM) interprets and executes this bytecode natively, achieving "Write Once, Run Anywhere" (WORA).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>Explain Garbage Collection in Java.</div>
    <div class="ans-body">
        <strong>Definition:</strong> Java features automatic memory management via the Garbage Collector (GC), a background daemon thread that periodically scans the Heap memory and deallocates memory occupied by unreachable (unreferenced) objects, preventing memory leaks without manual pointer freeing.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What is the purpose of the 'finally' block in Exception Handling?</div>
    <div class="ans-body">
        <strong>Definition:</strong> The <code>finally</code> block always executes regardless of whether an exception is thrown, caught, or unhandled. Used to perform critical resource clean-up actions such as closing file streams, database connections, and network sockets.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Differentiate between Abstract Class and Interface in Java with examples.</div>
    <div class="ans-body">
        <strong>Comparison:</strong>
        <table class="grid-table">
            <thead><tr><th>Aspect</th><th>Abstract Class</th><th>Interface</th></tr></thead>
            <tbody>
                <tr><td>Methods</td><td>Can have abstract and concrete methods with state.</td><td>Contains abstract methods (and default/static in Java 8+).</td></tr>
                <tr><td>Variables</td><td>Can have instance variables (any access modifier).</td><td>All fields are implicitly <code>public static final</code> constants.</td></tr>
                <tr><td>Inheritance</td><td>Single inheritance (a class <code>extends</code> only 1 abstract class).</td><td>Multiple inheritance (a class can <code>implements</code> multiple interfaces).</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain Exception Handling mechanism in Java with keywords: try, catch, finally, throw, and throws.</div>
    <div class="ans-body">
        <strong>Keywords & Mechanism:</strong>
        <ul>
            <li><code>try</code>: Encloses code that may potentially throw an exception.</li>
            <li><code>catch</code>: Catches and handles specific exception types.</li>
            <li><code>finally</code>: Guaranteed cleanup block executed after try/catch.</li>
            <li><code>throw</code>: Explicitly throws an exception object (e.g., <code>throw new ArithmeticException("Divide by zero");</code>).</li>
            <li><code>throws</code>: Declares exceptions in method signatures for callers to handle.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain the Applet Life Cycle and its core callback methods.</div>
    <div class="ans-body">
        <strong>Lifecycle Methods:</strong>
        <ol>
            <li><code>init()</code>: Called once when the applet is first loaded into the browser/appletviewer to initialize variables.</li>
            <li><code>start()</code>: Invoked every time the applet becomes visible or browser tab is opened.</li>
            <li><code>paint(Graphics g)</code>: Renders shapes, text, and images on the screen surface.</li>
            <li><code>stop()</code>: Invoked when the user leaves the page or minimizes the browser.</li>
            <li><code>destroy()</code>: Called before the applet is completely reclaimed from memory.</li>
        </ol>
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Write an HTML code to create a User Registration Web Form containing: Username, Date of Birth, Address, Gender (Radio buttons), Email-ID, Mobile Number, and Submit/Reset buttons.</div>
    <div class="ans-body">
        <strong>HTML Code:</strong>
<pre>
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;User Registration Form&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h2&gt;Student / User Registration Form&lt;/h2&gt;
    &lt;form action="register" method="POST"&gt;
        &lt;table cellpadding="6"&gt;
            &lt;tr&gt;
                &lt;td&gt;User Name:&lt;/td&gt;
                &lt;td&gt;&lt;input type="text" name="username" required /&gt;&lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;Date of Birth:&lt;/td&gt;
                &lt;td&gt;&lt;input type="date" name="dob" required /&gt;&lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;Address:&lt;/td&gt;
                &lt;td&gt;&lt;textarea name="address" rows="3" cols="30"&gt;&lt;/textarea&gt;&lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;Gender:&lt;/td&gt;
                &lt;td&gt;
                    &lt;input type="radio" name="gender" value="Male" /&gt; Male
                    &lt;input type="radio" name="gender" value="Female" /&gt; Female
                &lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;Email-ID:&lt;/td&gt;
                &lt;td&gt;&lt;input type="email" name="email" required /&gt;&lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;Mobile Number:&lt;/td&gt;
                &lt;td&gt;&lt;input type="tel" name="mobile" pattern="[0-9]{10}" required /&gt;&lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td colspan="2" align="center"&gt;
                    &lt;input type="submit" value="Register Now" /&gt;
                    &lt;input type="reset" value="Clear Form" /&gt;
                &lt;/td&gt;
            &lt;/tr&gt;
        &lt;/table&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>What is JDBC? Explain the Four Types of JDBC Drivers with architectural diagrams and characteristics.</div>
    <div class="ans-body">
        <strong>Definition:</strong> <strong>Java Database Connectivity (JDBC)</strong> is an industry-standard Java API that enables Java programs to interact with relational databases using SQL queries.<br><br>
        <strong>Four Types of JDBC Drivers:</strong>
        <ol>
            <li><strong>Type-1: JDBC-ODBC Bridge Driver:</strong> Translates JDBC calls to ODBC calls. Requires ODBC driver installation on every client machine. Obsolete and slow.</li>
            <li><strong>Type-2: Native-API / Partially Java Driver:</strong> Converts JDBC calls directly into native C/C++ vendor database client libraries (e.g., Oracle OCI). Requires client-side installation.</li>
            <li><strong>Type-3: Network Protocol / All-Java Middleware Driver:</strong> Translates JDBC calls into an intermediate server middleware protocol, which then talks to multiple databases. Flexible for 3-tier architectures.</li>
            <li><strong>Type-4: Thin Driver / Direct-to-Database Pure Java Driver:</strong> Converts JDBC calls directly into vendor-specific database network protocols via TCP/IP sockets. 100% pure Java, zero client installation, highest performance (Modern standard!).</li>
        </ol>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain Servlet Life Cycle and compare it with JSP Life Cycle. Write a complete HttpServlet code example.</div>
    <div class="ans-body">
        <strong>Servlet Life Cycle Methods:</strong>
        <ol>
            <li><code>init(ServletConfig config)</code>: Loads servlet class, creates instance, and initializes parameters (called once).</li>
            <li><code>service(HttpServletRequest req, HttpServletResponse res)</code>: Dispatches to <code>doGet()</code> or <code>doPost()</code> for every incoming HTTP request.</li>
            <li><code>destroy()</code>: Invoked when container unloads the servlet, releasing database and memory resources.</li>
        </ol>
        <strong>Servlet Implementation Example:</strong>
<pre>
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class WelcomeServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        String user = request.getParameter("username");
        out.println("&lt;html&gt;&lt;body&gt;");
        out.println("&lt;h2&gt;Welcome, " + user + "!&lt;/h2&gt;");
        out.println("&lt;p&gt;Server Response Time: " + new java.util.Date() + "&lt;/p&gt;");
        out.println("&lt;/body&gt;&lt;/html&gt;");
    }
}
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Define Thread in Java. Explain how to create threads using (a) Thread class and (b) Runnable interface. Write a complete multithreaded program.</div>
    <div class="ans-body">
        <strong>Multithreading in Java:</strong>
<pre>
// Approach 1: Extending Thread class
class NumberPrinter extends Thread {
    public void run() {
        for(int i = 1; i <= 5; i++) {
            System.out.println("Thread 1: " + i);
            try { Thread.sleep(500); } catch(Exception e) {}
        }
    }
}

// Approach 2: Implementing Runnable interface
class LetterPrinter implements Runnable {
    public void run() {
        for(char c = 'A'; c <= 'E'; c++) {
            System.out.println("Thread 2: " + c);
            try { Thread.sleep(500); } catch(Exception e) {}
        }
    }
}

public class MultiThreadDemo {
    public static void main(String[] args) {
        NumberPrinter t1 = new NumberPrinter();
        Thread t2 = new Thread(new LetterPrinter());
        t1.start(); // Spawns new thread
        t2.start();
    }
}
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>What are Layout Managers in AWT/Swing? Explain BorderLayout, FlowLayout, and GridLayout with examples.</div>
    <div class="ans-body">
        <strong>Layout Managers:</strong> Automatically position, size, and rearrange GUI components inside containers regardless of screen resolution or OS window scaling.<br>
        <ul>
            <li><strong>FlowLayout:</strong> Arranges components sequentially from left to right, wrapping to the next line when space runs out. Default for <code>Panel</code> and <code>Applet</code>.</li>
            <li><strong>BorderLayout:</strong> Divides container into 5 regions: <code>NORTH</code>, <code>SOUTH</code>, <code>EAST</code>, <code>WEST</code>, and <code>CENTER</code>. Default for <code>Frame</code> and <code>JFrame</code>.</li>
            <li><strong>GridLayout:</strong> Arranges components into a rectangular grid of equal-sized rows and columns.</li>
        </ul>
    </div>
</div>
"""

print("Generating Java 2025 PDF...")
generate_java_pdf("December 2025", "java 2025 solved.pdf", YEAR_2025_HTML)

# ==============================================================================
# YEAR 2024 (December 2024)
# ==============================================================================
YEAR_2024_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Discuss Primitive Data Types in Java.</div>
    <div class="ans-body">
        <strong>Java Data Types:</strong>
        <ul>
            <li><strong>Integer Types:</strong> <code>byte</code> (1 byte), <code>short</code> (2 bytes), <code>int</code> (4 bytes), <code>long</code> (8 bytes).</li>
            <li><strong>Floating-Point:</strong> <code>float</code> (4 bytes, IEEE 754), <code>double</code> (8 bytes).</li>
            <li><strong>Character:</strong> <code>char</code> (2 bytes, 16-bit Unicode character).</li>
            <li><strong>Boolean:</strong> <code>boolean</code> (represents true or false).</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Explain TCP/IP Server Socket in Java.</div>
    <div class="ans-body">
        <strong>Explanation:</strong> Java provides the <code>java.net.ServerSocket</code> class to implement a TCP server that listens for incoming connection requests on a designated port.
<pre>
ServerSocket server = new ServerSocket(8080);
Socket client = server.accept(); // Blocks until connection arrives
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>What are Packages? How do you call a package in Java?</div>
    <div class="ans-body">
        <strong>Definition:</strong> A <strong>Package</strong> is a namespace mechanism that organizes related classes and interfaces into modular directory structures, preventing naming conflicts and providing access protection.<br>
        <strong>Calling a Package:</strong> Uses the <code>import</code> keyword:
<pre>
import java.util.ArrayList; // Imports single class
import java.io.*;          // Imports all classes in package
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>Explain the Anchor and Table tags in HTML.</div>
    <div class="ans-body">
        <strong>HTML Tags:</strong>
        <ul>
            <li><code>&lt;a href="url"&gt;Link Text&lt;/a&gt;</code>: Creates a hyperlink to navigate between web pages or download files.</li>
            <li><code>&lt;table&gt;&lt;tr&gt;&lt;th&gt;...&lt;/th&gt;&lt;td&gt;...&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;</code>: Renders structured tabular data using rows (<code>&lt;tr&gt;</code>), headers (<code>&lt;th&gt;</code>), and data cells (<code>&lt;td&gt;</code>).</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>Briefly explain Internet Concepts: URL, HTTP, and Web Server.</div>
    <div class="ans-body">
        <strong>Concepts:</strong>
        <ul>
            <li><strong>URL (Uniform Resource Locator):</strong> Global address of a resource on the web (e.g., <code>https://www.example.com/index.html</code>).</li>
            <li><strong>HTTP:</strong> HyperText Transfer Protocol, a stateless client-server protocol running over TCP port 80/443 for web communication.</li>
            <li><strong>Web Server:</strong> Hardware/software that serves web resources to clients (Apache, Nginx, Tomcat).</li>
        </ul>
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Explain Applet Life Cycle. Write a program to demonstrate a simple Java applet to display an image. Compare Applets over HTML.</div>
    <div class="ans-body">
        <strong>Applet Image Display Code:</strong>
<pre>
import java.applet.*;
import java.awt.*;

/* &lt;applet code="ImageApplet.class" width="400" height="300"&gt;&lt;/applet&gt; */
public class ImageApplet extends Applet {
    Image img;
    public void init() {
        img = getImage(getDocumentBase(), "college_logo.png");
    }
    public void paint(Graphics g) {
        g.drawImage(img, 20, 20, this);
        g.drawString("CCSU BCA V Semester", 20, 260);
    }
}
</pre>
        <strong>Comparison over HTML:</strong> Applets provide dynamic client-side computation, graphical interactivity, and local state management that static HTML cannot natively provide.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain TCP/IP Client Socket. Write constructors and methods used to create client sockets.</div>
    <div class="ans-body">
        <strong>Client Socket (java.net.Socket):</strong>
        <ul>
            <li><strong>Constructors:</strong>
                <ul>
                    <li><code>Socket(String host, int port)</code> &mdash; Establishes TCP stream connection.</li>
                    <li><code>Socket(InetAddress address, int port)</code></li>
                </ul>
            </li>
            <li><strong>Methods:</strong>
                <ul>
                    <li><code>getInputStream()</code> &mdash; Returns InputStream for reading server responses.</li>
                    <li><code>getOutputStream()</code> &mdash; Returns OutputStream for sending data.</li>
                    <li><code>close()</code> &mdash; Gracefully closes the TCP connection.</li>
                </ul>
            </li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain the concepts of Inheritance in Java and its various types.</div>
    <div class="ans-body">
        <strong>Inheritance:</strong> The mechanism where a subclass derives attributes and behaviors from a superclass using <code>extends</code>.<br>
        <strong>Types in Java:</strong>
        <ol>
            <li><strong>Single Inheritance:</strong> Class B extends Class A.</li>
            <li><strong>Multilevel Inheritance:</strong> Class C extends Class B, which extends Class A.</li>
            <li><strong>Hierarchical Inheritance:</strong> Class B and Class C both extend Class A.</li>
            <li><strong>Multiple Inheritance:</strong> Achieved through <strong>Interfaces</strong> (Java does not support multiple class inheritance to avoid the Diamond Problem).</li>
        </ol>
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>What is JDBC? Write a complete JDBC program to insert and display records of employees using PreparedStatement.</div>
    <div class="ans-body">
        <strong>Complete PreparedStatement JDBC Program:</strong>
<pre>
import java.sql.*;

public class EmployeeJDBC {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/company_db";
        String user = "root";
        String password = "password";

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection(url, user, password);

            // 1. Insert record using PreparedStatement
            String insertSql = "INSERT INTO Employee(EmpID, Name, Salary) VALUES(?, ?, ?)";
            PreparedStatement psInsert = conn.prepareStatement(insertSql);
            psInsert.setInt(1, 101);
            psInsert.setString(2, "Rahul Sharma");
            psInsert.setDouble(3, 55000.00);
            int rows = psInsert.executeUpdate();
            System.out.println("Inserted rows: " + rows);

            // 2. Display all employee records
            String selectSql = "SELECT EmpID, Name, Salary FROM Employee";
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(selectSql);

            System.out.println("\n--- EMPLOYEE RECORDS ---");
            while(rs.next()) {
                System.out.println(rs.getInt("EmpID") + "\t" + 
                                   rs.getString("Name") + "\t" + 
                                   rs.getDouble("Salary"));
            }
            conn.close();
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>What are Packages? Explain Java API Packages. List any five methods of the String class with examples.</div>
    <div class="ans-body">
        <strong>String Class Methods:</strong>
        <ol>
            <li><code>length()</code>: Returns character count &rarr; <code>"Hello".length() == 5</code>.</li>
            <li><code>charAt(int index)</code>: Returns character at index &rarr; <code>"Hello".charAt(1) == 'e'</code>.</li>
            <li><code>substring(int begin, int end)</code>: Extracts substring &rarr; <code>"Java".substring(0, 2) == "Ja"</code>.</li>
            <li><code>toUpperCase()</code>: Converts to uppercase &rarr; <code>"bca".toUpperCase() == "BCA"</code>.</li>
            <li><code>equals(Object another)</code>: Compares string contents &rarr; <code>"Java".equals("Java") == true</code>.</li>
        </ol>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain Servlets with their Life Cycle. How is it different from the Life Cycle of JSP?</div>
    <div class="ans-body">
        <strong>Comparison:</strong>
        <ul>
            <li><strong>Servlet:</strong> Java class compiled into bytecode; container directly executes <code>init()</code>, <code>service()</code>, and <code>destroy()</code>.</li>
            <li><strong>JSP:</strong> Text-based document with HTML + embedded Java code; container first translates JSP into a temporary Java Servlet source file, compiles it to bytecode, and invokes <code>_jspInit()</code>, <code>_jspService()</code>, and <code>_jspDestroy()</code>.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Discuss JSP in detail. What are JSP Directives? Explain various types of directives with examples.</div>
    <div class="ans-body">
        <strong>JSP Directives (<code>&lt;%@ directive attribute="value" %&gt;</code>):</strong>
        <ol>
            <li><strong>page Directive:</strong> Controls page-level settings:
                <code>&lt;%@ page import="java.util.*, java.sql.*" contentType="text/html" errorPage="error.jsp" %&gt;</code>
            </li>
            <li><strong>include Directive:</strong> Inserts static files at translation time:
                <code>&lt;%@ include file="header.jsp" %&gt;</code>
            </li>
            <li><strong>taglib Directive:</strong> Imports custom tag libraries (JSTL):
                <code>&lt;%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %&gt;</code>
            </li>
        </ol>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>What are Layout Managers? Explain five Layout Managers supported by AWT/Swing.</div>
    <div class="ans-body">
        <strong>Five Layout Managers:</strong>
        <ol>
            <li><strong>FlowLayout:</strong> Arranges components row-by-row like words in a paragraph.</li>
            <li><strong>BorderLayout:</strong> Positions in North, South, East, West, Center regions.</li>
            <li><strong>GridLayout:</strong> Rectangular grid of equal-sized cells.</li>
            <li><strong>CardLayout:</strong> Stacks components like a deck of cards (one visible at a time).</li>
            <li><strong>GridBagLayout:</strong> Most flexible layout manager using <code>GridBagConstraints</code> for variable cell spans and weights.</li>
        </ol>
    </div>
</div>
"""

print("Generating Java 2024 PDF...")
generate_java_pdf("December 2024", "java 2024 solved.pdf", YEAR_2024_HTML)

# ==============================================================================
# YEAR 2023 (December 2023)
# ==============================================================================
YEAR_2023_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>How is an Object created in Java?</div>
    <div class="ans-body">
        <strong>Object Creation:</strong> Uses the <code>new</code> operator:
<pre>
ClassName obj = new ClassName();
</pre>
        Steps: (1) <em>Declaration</em> (associates variable name with object type), (2) <em>Instantiation</em> (<code>new</code> allocates memory on the Heap), (3) <em>Initialization</em> (invokes the constructor).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Compare JDK, JRE, and JVM.</div>
    <div class="ans-body">
        <strong>Relationship:</strong>
        <ul>
            <li><strong>JVM (Java Virtual Machine):</strong> The runtime engine that interprets and executes bytecode.</li>
            <li><strong>JRE (Java Runtime Environment):</strong> Contains JVM + Java Standard Class Libraries; sufficient to run Java programs.</li>
            <li><strong>JDK (Java Development Kit):</strong> Contains JRE + Development Tools (<code>javac</code>, <code>javadoc</code>, <code>jar</code>, <code>debugger</code>); needed to write and compile programs.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Difference between JDBC and ODBC.</div>
    <div class="ans-body">
        <strong>Differences:</strong> ODBC is a C/C++ platform-dependent API designed originally for Windows. JDBC is a platform-independent pure Java API tailored for Java applications and cross-platform RDBMS connectivity.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>Write differences between JSP and Servlet.</div>
    <div class="ans-body">
        <strong>Differences:</strong> Servlets are Java code with embedded HTML strings (ideal for business logic and controllers). JSP is HTML markup with embedded Java scriptlets (ideal for presentation and views in MVC).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What is Method Overloading vs Method Overriding?</div>
    <div class="ans-body">
        <strong>Comparison:</strong> Overloading occurs in the same class with identical method names but different parameter lists (compile-time polymorphism). Overriding occurs in subclasses with identical method signatures and return types (runtime dynamic dispatch).
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>What is an Applet? Describe the complete Life Cycle of an Applet.</div>
    <div class="ans-body">
        <strong>Applet Life Cycle:</strong> <code>init()</code> &rarr; <code>start()</code> &rarr; <code>paint(Graphics g)</code> &rarr; <code>stop()</code> &rarr; <code>destroy()</code>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain Interface in Java. How is multiple inheritance achieved using interfaces?</div>
    <div class="ans-body">
        <strong>Explanation:</strong> A class can implement multiple interfaces simultaneously:
<pre>
interface Printable { void print(); }
interface Showable { void show(); }
class Document implements Printable, Showable {
    public void print() { System.out.println("Printing..."); }
    public void show() { System.out.println("Showing..."); }
}
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain Exception Handling in Java with try-catch-finally block.</div>
    <div class="ans-body">
        <strong>Handling:</strong> Code capable of raising runtime exceptions is placed inside <code>try</code>, recovered in <code>catch</code>, and resource deallocation performed in <code>finally</code>.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>What are Packages in Java? How is a user-defined package created and imported? Explain with complete code example.</div>
    <div class="ans-body">
        <strong>Creating & Importing User-Defined Package:</strong>
<pre>
// File: mypack/Calculator.java
package mypack;

public class Calculator {
    public int add(int a, int b) { return a + b; }
    public int multiply(int a, int b) { return a * b; }
}

// File: TestPackage.java
import mypack.Calculator;

public class TestPackage {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        System.out.println("Sum: " + calc.add(10, 20));
        System.out.println("Product: " + calc.multiply(10, 20));
    }
}
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Define Thread. How to create a thread in Java? Write a program that executes two threads simultaneously.</div>
    <div class="ans-body">
        <strong>Complete Dual Thread Program:</strong>
<pre>
class ThreadOne extends Thread {
    public void run() {
        for(int i = 1; i <= 5; i++) {
            System.out.println("Thread 1 executing count: " + i);
            try { Thread.sleep(400); } catch(Exception e) {}
        }
    }
}

class ThreadTwo extends Thread {
    public void run() {
        for(int j = 10; j <= 15; j++) {
            System.out.println("Thread 2 executing count: " + j);
            try { Thread.sleep(400); } catch(Exception e) {}
        }
    }
}

public class DualThreadDemo {
    public static void main(String[] args) {
        ThreadOne t1 = new ThreadOne();
        ThreadTwo t2 = new ThreadTwo();
        t1.start();
        t2.start();
    }
}
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain JDBC Architecture and steps involved in connecting a Java application to a Database. Write complete program.</div>
    <div class="ans-body">
        <strong>Steps:</strong> (1) Load Driver, (2) Create Connection, (3) Create Statement, (4) Execute Query, (5) Process ResultSet, (6) Close Connection.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain HTML form controls and write code for an Admission Form.</div>
    <div class="ans-body">
        <strong>Admission Form:</strong> Includes text fields, dropdown selects, checkboxes, text areas, and submit buttons.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Explain JSP implicit objects and session tracking in Web Applications.</div>
    <div class="ans-body">
        <strong>Implicit Objects:</strong> <code>request</code>, <code>response</code>, <code>session</code>, <code>application</code>, <code>out</code>, <code>config</code>, <code>pageContext</code>, <code>page</code>, <code>exception</code>. Session tracking via Cookies, URL Rewriting, and HttpSession.
    </div>
</div>
"""

print("Generating Java 2023 PDF...")
generate_java_pdf("December 2023", "java 2023 solved.pdf", YEAR_2023_HTML)
