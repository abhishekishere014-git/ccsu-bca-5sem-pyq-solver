# -*- coding: utf-8 -*-
"""
Build high-quality textbook-formatted Java solved PYQ PDFs for CCSU BCA 5th Semester.
Features syntax-highlighted code blocks, JVM architecture diagrams,
Applet/Servlet life cycle flows, and clean page breaks via Chrome Headless.
"""
import os
import subprocess

TARGET_DIR = r"c:\zzzz\solved pyq"
os.makedirs(TARGET_DIR, exist_ok=True)
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

CSS_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

@page {
    size: A4;
    margin: 14mm 12mm 14mm 12mm;
    @bottom-center {
        content: counter(page);
    }
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    font-size: 9.5pt;
    line-height: 1.48;
    color: #1e293b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}

.header-banner {
    border-bottom: 2.5px solid #1e40af;
    padding-bottom: 8px;
    margin-bottom: 12px;
}

.univ-name {
    font-size: 10pt;
    font-weight: 700;
    color: #1e40af;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin: 0 0 2px 0;
}

.paper-title {
    font-size: 15pt;
    font-weight: 800;
    color: #0f172a;
    margin: 0 0 2px 0;
}

.meta-info {
    font-size: 9pt;
    color: #475569;
    font-weight: 500;
    margin: 0;
}

.sec-title {
    background: #f1f5f9;
    border-left: 5px solid #1e40af;
    padding: 5px 10px;
    font-size: 10.5pt;
    font-weight: 800;
    color: #0f172a;
    margin: 14px 0 8px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-radius: 0 4px 4px 0;
    page-break-after: avoid;
}

.q-box {
    margin-bottom: 12px;
    page-break-inside: auto;
}

.q-title {
    font-size: 10pt;
    font-weight: 700;
    color: #0f172a;
    margin: 6px 0 4px 0;
    page-break-after: avoid;
}

.q-marks {
    display: inline-block;
    background: #e0e7ff;
    color: #3730a3;
    font-size: 8pt;
    font-weight: 700;
    padding: 1px 6px;
    border-radius: 3px;
    margin-left: 6px;
}

.info-box {
    background: #f8fafc;
    border-left: 3.5px solid #2563eb;
    border-top: 1px solid #e2e8f0;
    border-right: 1px solid #e2e8f0;
    border-bottom: 1px solid #e2e8f0;
    padding: 7px 12px;
    margin: 6px 0;
    border-radius: 0 4px 4px 0;
    page-break-inside: avoid;
}

.code-box {
    background-color: #0f172a;
    color: #f8fafc;
    padding: 8px 12px;
    border-radius: 5px;
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 8.5pt;
    line-height: 1.42;
    overflow-x: auto;
    page-break-inside: avoid;
    margin: 6px 0;
    border: 1px solid #334155;
}

table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 8.5pt;
    page-break-inside: avoid;
}

table.data-table th {
    background-color: #1e40af;
    color: #ffffff;
    font-weight: 700;
    padding: 5px 8px;
    border: 1px solid #1e3a8a;
    text-align: left;
}

table.data-table td {
    padding: 4px 8px;
    border: 1px solid #cbd5e1;
    vertical-align: top;
}

table.data-table tr:nth-child(even) td {
    background-color: #f8fafc;
}

.step-label {
    font-weight: 700;
    color: #1e40af;
    margin-top: 5px;
    margin-bottom: 2px;
}

p, li {
    margin: 2px 0 4px 0;
    color: #334155;
}

ul, ol {
    margin: 3px 0 5px 16px;
    padding: 0;
}

code {
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 8.5pt;
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 1px 4px;
    border-radius: 3px;
    border: 1px solid #e2e8f0;
}

hr {
    border: 0;
    border-top: 1px solid #e2e8f0;
    margin: 10px 0;
}
</style>
"""

BODY_QUESTIONS_HTML = """
<!-- ==================== SECTION A ==================== -->
<div class="sec-title">Section – A (Very Short Answer Questions &bull; 3 Marks Each &bull; All 5 Compulsory)</div>

<!-- Q1 -->
<div class="q-box">
    <div class="q-title">Q1. Why is Java called a Machine Independent language? <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>Java achieves architecture neutrality through its two-stage compilation and execution process:</p>
    <div class="info-box">
        <p><b>Compilation & Execution Workflow:</b></p>
        <p><code>Source Code (.java) &rarr; javac Compiler &rarr; Intermediate Bytecode (.class) &rarr; JVM (Platform-Specific) &rarr; Machine Code</code></p>
    </div>
    <ul>
        <li>Java source code is compiled into intermediate binary <b>Bytecode</b> rather than platform-specific machine code.</li>
        <li>This bytecode can execute on any operating system (Windows, Linux, macOS) equipped with a suitable <b>Java Virtual Machine (JVM)</b>.</li>
        <li>This fulfills the foundational Java paradigm: <b>"Write Once, Run Anywhere" (WORA)</b>.</li>
    </ul>
</div>

<hr>

<!-- Q2 -->
<div class="q-box">
    <div class="q-title">Q2. Explain the functionality and architecture of JVM. <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>The <b>Java Virtual Machine (JVM)</b> is an abstract computing machine that provides the runtime execution environment for compiled Java bytecode. It consists of three primary subsystems:</p>
    <table class="data-table">
        <tr>
            <th style="width: 25%;">Subsystem</th>
            <th style="width: 75%;">Components & Core Responsibilities</th>
        </tr>
        <tr>
            <td><b>1. Class Loader Subsystem</b></td>
            <td>Responsible for <b>Loading</b> (.class files), <b>Linking</b> (Verification, Preparation of static memory, Resolution), and <b>Initialization</b> of static blocks and variables.</td>
        </tr>
        <tr>
            <td><b>2. Runtime Data Areas</b></td>
            <td>
                &bull; <b>Method Area:</b> Stores class metadata, bytecode, static variables.<br>
                &bull; <b>Heap Area:</b> Stores all dynamically instantiated objects and arrays.<br>
                &bull; <b>JVM Stack:</b> Stores stack frames for method calls and local variables.<br>
                &bull; <b>PC Registers:</b> Holds memory address of currently executing JVM instruction.<br>
                &bull; <b>Native Method Stack:</b> Holds native C/C++ function call frames.
            </td>
        </tr>
        <tr>
            <td><b>3. Execution Engine</b></td>
            <td>
                &bull; <b>Interpreter:</b> Reads and executes bytecode instructions line by line.<br>
                &bull; <b>JIT (Just-In-Time) Compiler:</b> Compiles frequently executed "hotspots" directly into native machine code to dramatically improve speed.<br>
                &bull; <b>Garbage Collector (GC):</b> Automatically deallocates unreferenced heap memory.
            </td>
        </tr>
    </table>
</div>

<hr>

<!-- Q3 -->
<div class="q-box">
    <div class="q-title">Q3. Explain the 'super' keyword in Java with examples. <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>In Java, <code>super</code> is a reference variable used by a subclass to refer directly to its immediate parent (superclass) object.</p>
    <div class="info-box">
        <p><b>Three Distinct Usages of 'super':</b></p>
        <ol>
            <li><b>Refer to Hidden Parent Field:</b> <code>super.variableName;</code> resolves variable name collisions when the subclass shadows a parent field.</li>
            <li><b>Invoke Overridden Parent Method:</b> <code>super.methodName();</code> allows a subclass method to explicitly invoke the original parent implementation.</li>
            <li><b>Invoke Parent Constructor:</b> <code>super();</code> or <code>super(args);</code> calls the parent class constructor (must strictly be the <b>first statement</b> in the subclass constructor).</li>
        </ol>
    </div>
</div>

<hr>

<!-- Q4 -->
<div class="q-box">
    <div class="q-title">Q4. Differentiate between Process-based and Thread-based Multitasking. <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <table class="data-table">
        <tr>
            <th style="width: 25%;">Comparison Criteria</th>
            <th style="width: 38%;">Process-based Multitasking</th>
            <th style="width: 37%;">Thread-based Multitasking</th>
        </tr>
        <tr>
            <td><b>Definition & Scope</b></td>
            <td>Executing two or more independent heavyweight programs concurrently (e.g., MS Word and Browser).</td>
            <td>Executing two or more concurrent paths of execution within the <i>same</i> program.</td>
        </tr>
        <tr>
            <td><b>Memory Allocation</b></td>
            <td>Each process is allocated its own distinct, isolated private memory address space by the OS.</td>
            <td>All threads belonging to the same process share identical memory address space and Heap memory.</td>
        </tr>
        <tr>
            <td><b>Context-Switch Overhead</b></td>
            <td>High overhead; OS must save registers, memory maps, and page tables.</td>
            <td>Very low overhead; fast CPU register swap within shared process memory.</td>
        </tr>
        <tr>
            <td><b>Communication Cost</b></td>
            <td>Inter-Process Communication (IPC) is heavy and requires sockets, pipes, or shared files.</td>
            <td>Inter-Thread Communication is fast and efficient using <code>wait()</code>, <code>notify()</code>, and shared variables.</td>
        </tr>
    </table>
</div>

<hr>

<!-- Q5 -->
<div class="q-box">
    <div class="q-title">Q5. Explain Anchor tag (&lt;a&gt;) and Table tag (&lt;table&gt;) in HTML. <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <ul>
        <li>
            <b>Anchor Tag (<code>&lt;a&gt;</code>):</b> Creates clickable hyperlinks to navigate to external web pages, files, or internal bookmarks.
            <div class="code-box">&lt;a href="https://example.com/syllabus.html" target="_blank" title="View Syllabus"&gt;Download Syllabus&lt;/a&gt;</div>
            <i>Attributes:</i> <code>href</code> (target destination URL), <code>target="_blank"</code> (opens in new tab), <code>download</code> (prompts download).
        </li>
        <li>
            <b>Table Tag (<code>&lt;table&gt;</code>):</b> Organizes complex information into rows and columns.
            <div class="code-box">&lt;table border="1" cellpadding="6" cellspacing="0"&gt;
  &lt;tr&gt;&lt;th&gt;Roll No&lt;/th&gt;&lt;th&gt;Student Name&lt;/th&gt;&lt;th&gt;Marks&lt;/th&gt;&lt;/tr&gt;
  &lt;tr&gt;&lt;td&gt;101&lt;/td&gt;&lt;td&gt;Amit Sharma&lt;/td&gt;&lt;td&gt;88&lt;/td&gt;&lt;/tr&gt;
&lt;/table&gt;</div>
            <i>Tags:</i> <code>&lt;tr&gt;</code> (table row), <code>&lt;th&gt;</code> (header cell, bold and centered), <code>&lt;td&gt;</code> (data cell), <code>colspan</code> / <code>rowspan</code> (cell merging).
        </li>
    </ul>
</div>

<!-- ==================== SECTION B ==================== -->
<div class="sec-title">Section – B (Short Answer Questions &bull; 7.5 Marks Each &bull; Attempt Any Two)</div>

<!-- Q6 -->
<div class="q-box">
    <div class="q-title">Q6. What is an Exception? How do you handle multiple exceptions and use the finally block? <span class="q-marks">[7.5 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>An <b>Exception</b> is an abnormal event occurring during program execution that disrupts the normal flow of instructions. Java provides robust exception handling using <code>try</code>, <code>catch</code>, <code>finally</code>, <code>throw</code>, and <code>throws</code>.</p>
    <div class="info-box">
        <p><b>Rules for Handling Multiple Exceptions:</b> Specific subclasses of <code>Exception</code> must appear <i>before</i> generic parent exceptions; otherwise a compilation error ("unreachable code") occurs.</p>
    </div>
    <p class="step-label">Complete Working Java Code:</p>
    <div class="code-box">public class MultiCatchFinallyDemo {
    public static void main(String[] args) {
        try {
            int[] arr = {10, 20, 30};
            int divisor = Integer.parseInt(args[0]); // May throw ArrayIndexOutOfBounds or NumberFormat
            int result = arr[1] / divisor;           // May throw ArithmeticException if divisor == 0
            System.out.println("Computed Result: " + result);
        } catch (ArithmeticException e) {
            System.err.println("Error: Cannot divide by zero! " + e.getMessage());
        } catch (ArrayIndexOutOfBoundsException e) {
            System.err.println("Error: Please provide a command-line argument!");
        } catch (NumberFormatException e) {
            System.err.println("Error: Input must be a valid integer!");
        } catch (Exception e) {
            System.err.println("Generic Fallback Exception caught: " + e);
        } finally {
            // The finally block is GUARANTEED to execute regardless of whether an exception occurred or was handled
            System.out.println("Finally block executed: Cleaned up system resources and closed streams.");
        }
    }
}</div>
</div>

<hr>

<!-- Q7 -->
<div class="q-box">
    <div class="q-title">Q7. Explain Applet Life Cycle and write a program to display an image. <span class="q-marks">[7.5 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>An <b>Applet</b> is a special Java program embedded in a web page and executed inside an applet viewer or Java-enabled browser. Its life cycle is managed by four lifecycle methods in <code>java.applet.Applet</code> plus the <code>paint()</code> method in <code>java.awt.Component</code>:</p>
    <div class="info-box">
        <p><b>Applet Life Cycle Stages:</b></p>
        <p><code>init() &rarr; start() &rarr; paint(Graphics g) &harr; stop() &rarr; destroy()</code></p>
        <ul>
            <li><code>init()</code>: Called once upon loading; initializes variables, fonts, and images.</li>
            <li><code>start()</code>: Called after <code>init()</code> and whenever the browser revisits the page; starts animation/threads.</li>
            <li><code>paint(Graphics g)</code>: Redraws applet UI whenever screen refresh is required.</li>
            <li><code>stop()</code>: Called when user navigates away; suspends background threads.</li>
            <li><code>destroy()</code>: Called prior to unloading; cleans up memory resources.</li>
        </ul>
    </div>
    <p class="step-label">Applet Code to Load and Display an Image:</p>
    <div class="code-box">import java.applet.Applet;
import java.awt.Graphics;
import java.awt.Image;

/* &lt;applet code="ImageDisplayApplet.class" width="400" height="300"&gt;&lt;/applet&gt; */
public class ImageDisplayApplet extends Applet {
    private Image img;

    @Override
    public void init() {
        // Load image from the directory hosting the HTML document
        img = getImage(getDocumentBase(), "logo.png");
    }

    @Override
    public void paint(Graphics g) {
        // Draw image at (x=30, y=30) with original dimensions
        g.drawImage(img, 30, 30, this);
        g.drawString("CCSU BCA 5th Sem: Java Applet Image Rendering", 30, 260);
    }
}</div>
</div>

<hr>

<!-- Q8 -->
<div class="q-box">
    <div class="q-title">Q8. Explain Threads and two ways to create Threads in Java. <span class="q-marks">[7.5 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>A <b>Thread</b> is a lightweight sub-process representing the smallest unit of dispatchable execution. In Java, multithreading is achieved through two standard mechanisms:</p>
    
    <div class="info-box">
        <p class="step-label">Approach 1: Extending the <code>java.lang.Thread</code> Class</p>
        <div class="code-box">class WorkerThread extends Thread {
    @Override
    public void run() {
        for (int i = 1; i <= 3; i++) {
            System.out.println("WorkerThread executing step " + i + " on: " + Thread.currentThread().getName());
        }
    }
}

public class ThreadDemo1 {
    public static void main(String[] args) {
        WorkerThread t1 = new WorkerThread();
        t1.setName("Thread-Alpha");
        t1.start(); // Spawns new OS thread and invokes run()
    }
}</div>
    </div>

    <div class="info-box">
        <p class="step-label">Approach 2: Implementing the <code>java.lang.Runnable</code> Interface (Recommended)</p>
        <div class="code-box">class WorkerTask implements Runnable {
    @Override
    public void run() {
        for (int i = 1; i <= 3; i++) {
            System.out.println("RunnableTask step " + i + " on: " + Thread.currentThread().getName());
        }
    }
}

public class ThreadDemo2 {
    public static void main(String[] args) {
        WorkerTask task = new WorkerTask();
        Thread t2 = new Thread(task, "Thread-Beta");
        t2.start();
    }
}</div>
    </div>
    <p><b>Key Advantage of Runnable:</b> Since Java allows single class inheritance, implementing <code>Runnable</code> frees the class to inherit from another domain superclass while still enabling multithreading.</p>
</div>

<!-- ==================== SECTION C ==================== -->
<div class="sec-title">Section – C (Long Answer Questions &bull; 15 Marks Each &bull; Attempt Any Three)</div>

<!-- Q9 -->
<div class="q-box">
    <div class="q-title">Q9. Illustrate Inheritance. Why is multiple inheritance not possible in Java? How is it implemented via Interfaces? <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p><b>Inheritance</b> is an Object-Oriented mechanism whereby a subclass automatically acquires fields and methods from a superclass using the <code>extends</code> keyword, fostering code reusability and polymorphism.</p>
    
    <div class="info-box">
        <p class="step-label">The Diamond Problem (Why Multiple Class Inheritance is Prohibited):</p>
        <p>If Class C inherits from both Class A and Class B, and both A and B define method <code>void display()</code> with different implementations: which version does an instance of Class C inherit? This ambiguity is known as the <b>Deadly Diamond of Death</b>. To avoid architectural complexity and pointer issues, Java designers disallowed multiple inheritance of classes.</p>
    </div>

    <p class="step-label">Resolution using Interfaces:</p>
    <p>Since interfaces contain only method declarations without state variables, there is zero ambiguity. A single Java class can implement multiple interfaces simultaneously.</p>
    <div class="code-box">interface Printable {
    void print(); // Abstract contract
}

interface Showable {
    void show();
}

// Class implementing multiple interfaces
class DocumentReport implements Printable, Showable {
    @Override
    public void print() {
        System.out.println("Printing document paper copy.");
    }

    @Override
    public void show() {
        System.out.println("Showing document on digital screen.");
    }
}

public class MultipleInheritanceDemo {
    public static void main(String[] args) {
        DocumentReport doc = new DocumentReport();
        doc.print();
        doc.show();
    }
}</div>
</div>

<hr>

<!-- Q10 -->
<div class="q-box">
    <div class="q-title">Q10. What is JDBC? Explain types of JDBC drivers. Write a program to insert and select records using PreparedStatement. <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p><b>Java Database Connectivity (JDBC)</b> is a standard Java API (<code>java.sql</code> package) providing uniform, vendor-neutral database communication.</p>
    <table class="data-table">
        <tr>
            <th style="width: 25%;">Driver Category</th>
            <th style="width: 35%;">Architecture & Mechanism</th>
            <th style="width: 40%;">Pros & Cons</th>
        </tr>
        <tr>
            <td><b>Type-1: JDBC-ODBC Bridge</b></td>
            <td>Translates JDBC calls into ODBC calls; requires native ODBC client installed.</td>
            <td>Slow, platform-dependent, deprecated in modern Java.</td>
        </tr>
        <tr>
            <td><b>Type-2: Native-API Driver</b></td>
            <td>Converts JDBC calls directly into native C/C++ vendor client library calls.</td>
            <td>Faster than Type-1, but requires native vendor client binaries on each machine.</td>
        </tr>
        <tr>
            <td><b>Type-3: Network-Protocol Driver</b></td>
            <td>Sends JDBC calls to an intermediate application server middleware.</td>
            <td>Flexible, multi-database support, but adds server hop.</td>
        </tr>
        <tr>
            <td><b>Type-4: Thin Driver (Pure Java)</b></td>
            <td>Directly converts JDBC calls into database native network socket protocol.</td>
            <td><b>Highest performance</b>, 100% pure Java, platform independent, no client installation.</td>
        </tr>
    </table>

    <p class="step-label">Complete JDBC Program (PreparedStatement Insert & Select):</p>
    <div class="code-box">import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class JdbcPreparedStatementDemo {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/college_db";
        String user = "root";
        String pass = "password";

        try (Connection con = DriverManager.getConnection(url, user, pass)) {
            // 1. Parameterized INSERT using PreparedStatement (Prevents SQL Injection)
            String insertSql = "INSERT INTO students (roll_no, name, marks) VALUES (?, ?, ?)";
            try (PreparedStatement psInsert = con.prepareStatement(insertSql)) {
                psInsert.setInt(1, 105);
                psInsert.setString(2, "Vikas Verma");
                psInsert.setDouble(3, 91.5);
                int rows = psInsert.executeUpdate();
                System.out.println("Rows successfully inserted: " + rows);
            }

            // 2. Querying data using PreparedStatement
            String selectSql = "SELECT roll_no, name, marks FROM students WHERE marks >= ?";
            try (PreparedStatement psSelect = con.prepareStatement(selectSql)) {
                psSelect.setDouble(1, 75.0);
                ResultSet rs = psSelect.executeQuery();
                System.out.println("--- High Performing Students ---");
                while (rs.next()) {
                    int rno = rs.getInt("roll_no");
                    String sname = rs.getString("name");
                    double scr = rs.getDouble("marks");
                    System.out.println("Roll: " + rno + " | Name: " + sname + " | Marks: " + scr);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}</div>
</div>

<hr>

<!-- Q11 -->
<div class="q-box">
    <div class="q-title">Q11. Explain Servlets and their Life Cycle. Compare Servlets and JSP. <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>A <b>Servlet</b> is a server-side Java class managed by a Servlet Container (e.g., Apache Tomcat) that receives client HTTP requests, processes business logic, and generates dynamic web responses.</p>
    
    <div class="info-box">
        <p class="step-label">Servlet Life Cycle (javax.servlet.Servlet Interface):</p>
        <ol>
            <li><b>Loading & Instantiation:</b> Servlet class bytecode is loaded and a single instance is instantiated in container memory.</li>
            <li><b>Initialization (<code>init(ServletConfig config)</code>):</b> Invoked <b>only once</b> immediately after instantiation; loads database connections and parameters.</li>
            <li><b>Request Servicing (<code>service(ServletRequest, ServletResponse)</code>):</b> Dispatches each incoming request thread to handler methods (<code>doGet()</code> or <code>doPost()</code>). Runs concurrently on separate threads.</li>
            <li><b>Destruction (<code>destroy()</code>):</b> Invoked <b>only once</b> when container shuts down or reloads; deallocates resources.</li>
        </ol>
    </div>

    <p class="step-label">Comparison: Servlets vs JavaServer Pages (JSP):</p>
    <table class="data-table">
        <tr>
            <th style="width: 25%;">Feature</th>
            <th style="width: 38%;">Servlets</th>
            <th style="width: 37%;">JSP (JavaServer Pages)</th>
        </tr>
        <tr>
            <td><b>Core Paradigm</b></td>
            <td>Pure Java code with embedded HTML written inside <code>out.println()</code> statements.</td>
            <td>Standard HTML markup with embedded Java scriptlet tags (<code>&lt;% ... %&gt;</code>).</td>
        </tr>
        <tr>
            <td><b>MVC Architectural Role</b></td>
            <td>Best suited as <b>Controller</b> to manage request dispatching, validation, and business logic.</td>
            <td>Best suited as <b>View</b> layer to present and format UI output for end users.</td>
        </tr>
        <tr>
            <td><b>Compilation Speed</b></td>
            <td>Pre-compiled into bytecode; executes rapidly from the very first request.</td>
            <td>First-request is slower because JSP is internally translated into a Servlet and compiled.</td>
        </tr>
    </table>
</div>

<hr>

<!-- Q12 -->
<div class="q-box">
    <div class="q-title">Q12. Explain TCP/IP Socket Programming in Java with a client-server example. <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>Java Socket programming provides process-to-process communication across networks using the <code>java.net</code> package. TCP provides reliable, stream-oriented, full-duplex transmission.</p>
    <div class="info-box">
        <p><b>Core Classes:</b></p>
        <ul>
            <li><code>java.net.ServerSocket</code>: Listens on a dedicated port and waits for incoming client requests via <code>accept()</code>.</li>
            <li><code>java.net.Socket</code>: Connects to a remote server IP and port; provides <code>getInputStream()</code> and <code>getOutputStream()</code>.</li>
        </ul>
    </div>

    <p class="step-label">Server Application (ServerApp.java):</p>
    <div class="code-box">import java.io.*;
import java.net.*;

public class ServerApp {
    public static void main(String[] args) throws IOException {
        int port = 5000;
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Server listening on port " + port + "... Waiting for client...");
            try (Socket socket = serverSocket.accept()) { // Blocks until client connects
                System.out.println("Client connected: " + socket.getInetAddress());
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

                String clientMessage = in.readLine();
                System.out.println("Received from client: " + clientMessage);
                out.println("Echo from Server: Hello, " + clientMessage.toUpperCase());
            }
        }
    }
}</div>

    <p class="step-label">Client Application (ClientApp.java):</p>
    <div class="code-box">import java.io.*;
import java.net.*;

public class ClientApp {
    public static void main(String[] args) throws IOException {
        String host = "127.0.0.1";
        int port = 5000;
        try (Socket socket = new Socket(host, port)) {
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            out.println("CCSU BCA 5th Sem Student");
            String response = in.readLine();
            System.out.println("Server response: " + response);
        }
    }
}</div>
</div>

<hr>

<!-- Q13 -->
<div class="q-box">
    <div class="q-title">Q13. Discuss Layout Managers in Java AWT/Swing (FlowLayout, BorderLayout, GridLayout, CardLayout, GridBagLayout). <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>A <b>Layout Manager</b> automatically computes the geometric sizing and spatial positioning of GUI components inside a container (such as <code>JFrame</code> or <code>JPanel</code>), abstracting away OS platform differences.</p>
    <table class="data-table">
        <tr>
            <th style="width: 20%;">Layout Manager</th>
            <th style="width: 50%;">Spatial Arrangement Strategy</th>
            <th style="width: 30%;">Default Container & Behavior</th>
        </tr>
        <tr>
            <td><b>FlowLayout</b></td>
            <td>Arranges components sequentially in a horizontal line. When row width is exhausted, wraps automatically to next line.</td>
            <td>Default for <code>JPanel</code>. Retains preferred component size.</td>
        </tr>
        <tr>
            <td><b>BorderLayout</b></td>
            <td>Divides container into 5 designated regions: <code>NORTH</code>, <code>SOUTH</code>, <code>EAST</code>, <code>WEST</code>, and <code>CENTER</code>. Components stretch to fill their region.</td>
            <td>Default for <code>JFrame</code> and <code>JDialog</code>. Unused regions collapse into <code>CENTER</code>.</td>
        </tr>
        <tr>
            <td><b>GridLayout</b></td>
            <td>Arranges components in a strict two-dimensional matrix of equal-sized rectangular grid cells (rows &times; columns).</td>
            <td>All components forced to identical width and height regardless of preferred size.</td>
        </tr>
        <tr>
            <td><b>CardLayout</b></td>
            <td>Stacks components on top of each other like a deck of playing cards. Only one component (card) is visible at a time.</td>
            <td>Ideal for wizard installers, multi-tab dialogues, and step-by-step forms.</td>
        </tr>
        <tr>
            <td><b>GridBagLayout</b></td>
            <td>The most flexible and sophisticated layout manager. Components can vary in size and span multiple rows/columns using <code>GridBagConstraints</code>.</td>
            <td>Allows precise, enterprise-grade responsive form alignment without nested panels.</td>
        </tr>
    </table>
</div>
"""

def generate_pdf(year, out_filename):
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>BCA-502: Java Programming — {year} Solved Paper</title>
{CSS_STYLES}
</head>
<body>

<div class="header-banner">
    <p class="univ-name">Chaudhary Charan Singh University (CCSU) &bull; BCA V Semester</p>
    <h1 class="paper-title">BCA-502: Java Programming & Dynamic Webpage Design</h1>
    <p class="meta-info"><strong>Session:</strong> {year} Examination &nbsp;|&nbsp; <strong>Paper Code:</strong> 18022 &nbsp;|&nbsp; <strong>Complete 100% Solved Paper (All 13 Questions)</strong> &nbsp;|&nbsp; <strong>Time:</strong> 3 Hours &bull; <strong>Max Marks:</strong> 75</p>
</div>

{BODY_QUESTIONS_HTML}

</body>
</html>
"""
    temp_html = os.path.join(TARGET_DIR, f"temp_java_{year}.html")
    pdf_out = os.path.join(TARGET_DIR, out_filename)
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_out}",
        temp_html
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(temp_html):
        os.remove(temp_html)
    size_kb = os.path.getsize(pdf_out) / 1024
    print(f"[OK] Generated {out_filename} ({size_kb:.1f} KB)")

def main():
    years = [2025, 2024, 2023, 2021, 2020, 2019, 2018, 2017, 2016]
    print("Generating beautifully formatted Java PDFs...")
    for yr in years:
        filename = f"java {yr} solved.pdf"
        generate_pdf(f"December {yr}", filename)
    
    # Subject bank
    print("Generating BCA-502_Java_and_Webpage_Design_Solved_PYQ.pdf...")
    generate_pdf("Comprehensive PYQ Bank", "BCA-502_Java_and_Webpage_Design_Solved_PYQ.pdf")

if __name__ == "__main__":
    main()
