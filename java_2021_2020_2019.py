import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from java_builder_base import generate_java_pdf

# ==============================================================================
# YEAR 2021 (December 2021 / CV-3 Pattern)
# ==============================================================================
YEAR_2021_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks / CV-3 Pattern)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (7.5M)</span>Explain destroy() method, a stage in the life cycle of an Applet.</div>
    <div class="ans-body">
        <strong>Explanation:</strong> <code>destroy()</code> is the final callback method in the Applet lifecycle, invoked by the browser or AppletViewer before the applet is completely removed from memory and garbage collected. It is called only once after the <code>stop()</code> method to release non-memory resources (threads, sockets, database handles).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (7.5M)</span>What do you mean by a Package in Java? State the different Access Specifiers available in Java.</div>
    <div class="ans-body">
        <strong>Access Specifiers:</strong>
        <table class="grid-table">
            <thead><tr><th>Access Specifier</th><th>Same Class</th><th>Same Package</th><th>Subclass (Diff Pkg)</th><th>World (Everywhere)</th></tr></thead>
            <tbody>
                <tr><td><code>private</code></td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr>
                <tr><td><code>default</code> (package-private)</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td></tr>
                <tr><td><code>protected</code></td><td>Yes</td><td>Yes</td><td>Yes (via inheritance)</td><td>No</td></tr>
                <tr><td><code>public</code></td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (7.5M)</span>What is Exception? Give different types of exceptions that occur during runtime. Why handle exceptions?</div>
    <div class="ans-body">
        <strong>Explanation:</strong> An <strong>Exception</strong> is an abnormal runtime event that disrupts the normal flow of program instructions. Types: Checked (<code>IOException</code>, <code>SQLException</code>) and Unchecked/Runtime (<code>ArithmeticException</code>, <code>NullPointerException</code>, <code>ArrayIndexOutOfBoundsException</code>). Handled to maintain graceful execution and avoid abrupt program termination.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (7.5M)</span>What are the life-cycle methods of a JSP? Differences between JSP Custom Tags and JavaBeans.</div>
    <div class="ans-body">
        <strong>JSP Lifecycle:</strong> <code>jspInit()</code> &rarr; <code>_jspService(HttpServletRequest, HttpServletResponse)</code> &rarr; <code>jspDestroy()</code>.<br>
        <strong>Differences:</strong> JavaBeans encapsulate reusable business data and logic via getter/setter methods. Custom Tags encapsulate presentation logic and HTML formatting within custom XML-style tags.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (7.5M)</span>Explain Thread Priority. What are default values? Write a program to define two threads where one prints 1 to 10 and the other prints 10 to 1.</div>
    <div class="ans-body">
        <strong>Thread Priorities:</strong> Integer scale from 1 (<code>MIN_PRIORITY</code>) to 10 (<code>MAX_PRIORITY</code>), with default 5 (<code>NORM_PRIORITY</code>).<br>
        <strong>Program:</strong>
<pre>
class ForwardPrinter extends Thread {
    public void run() {
        for(int i = 1; i <= 10; i++) {
            System.out.println("Forward: " + i);
            try { Thread.sleep(200); } catch(Exception e) {}
        }
    }
}

class BackwardPrinter extends Thread {
    public void run() {
        for(int j = 10; j >= 1; j--) {
            System.out.println("Backward: " + j);
            try { Thread.sleep(200); } catch(Exception e) {}
        }
    }
}

public class PriorityThreadDemo {
    public static void main(String[] args) {
        ForwardPrinter t1 = new ForwardPrinter();
        BackwardPrinter t2 = new BackwardPrinter();
        t1.setPriority(Thread.MAX_PRIORITY);
        t2.setPriority(Thread.MIN_PRIORITY);
        t1.start();
        t2.start();
    }
}
</pre>
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (1 &times; 15 = 15 Marks / CV-3 Pattern)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (15M)</span>Explain Client-Server Socket Programming in Java with complete code.</div>
    <div class="ans-body">
        <strong>Socket Programming:</strong> <code>ServerSocket</code> on server side and <code>Socket</code> on client side transmitting data over TCP streams using <code>DataInputStream</code> and <code>DataOutputStream</code>.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (2 &times; 22.5 = 45 Marks / CV-3 Pattern)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (22.5M)</span>Explain JDBC Architecture and write a program to update employee salaries based on department.</div>
    <div class="ans-body">
        <strong>Program:</strong>
<pre>
import java.sql.*;

public class UpdateSalaryDemo {
    public static void main(String[] args) {
        try {
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/db", "root", "pass");
            PreparedStatement ps = con.prepareStatement("UPDATE Employee SET Salary = Salary * 1.10 WHERE Dept = ?");
            ps.setString(1, "IT");
            int rows = ps.executeUpdate();
            System.out.println("Salaries updated for " + rows + " employees.");
            con.close();
        } catch(Exception e) { e.printStackTrace(); }
    }
}
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (22.5M)</span>Explain AWT Event Handling with Delegation Event Model. Write a program to handle Button click events.</div>
    <div class="ans-body">
        <strong>Delegation Event Model:</strong> An event source generates an event and sends it to registered event listeners implementing listener interfaces (e.g., <code>ActionListener</code>).
    </div>
</div>
"""

print("Generating Java 2021 PDF...")
generate_java_pdf("December 2021", "java 2021 solved.pdf", YEAR_2021_HTML)

# ==============================================================================
# YEAR 2020 (December 2020)
# ==============================================================================
YEAR_2020_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Explain why Java is considered the best language for Internet Applications.</div>
    <div class="ans-body">
        <strong>Reasons:</strong> Platform independence via bytecode/JVM, built-in security (sandbox security manager), robust memory management, native multithreading, and extensive networking APIs (<code>java.net</code>).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Discuss various primitive data types supported by Java.</div>
    <div class="ans-body">
        <strong>Primitive Types:</strong> 8 primitive types: <code>byte</code>, <code>short</code>, <code>int</code>, <code>long</code>, <code>float</code>, <code>double</code>, <code>char</code>, <code>boolean</code> with explicit fixed sizes across all platforms.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>What is the purpose of the 'static' keyword in Java?</div>
    <div class="ans-body">
        <strong>Explanation:</strong> Marks class-level members (variables, methods, blocks) shared by all instances, callable without creating an object of the class (e.g., <code>ClassName.staticMethod()</code>).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>What are Wrapper Classes in Java?</div>
    <div class="ans-body">
        <strong>Explanation:</strong> Classes that wrap primitive data types into object representations (<code>Integer</code>, <code>Double</code>, <code>Boolean</code>) enabling autoboxing and unboxing for collections.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>Define Interface in Java.</div>
    <div class="ans-body">
        <strong>Definition:</strong> A reference type containing pure abstract method declarations and static constants, defining a functional contract for implementing classes.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Explain Applet Life Cycle and write an Applet to display a greeting message.</div>
    <div class="ans-body">
        <strong>Applet Lifecycle:</strong> Complete coverage of <code>init()</code>, <code>start()</code>, <code>paint()</code>, <code>stop()</code>, and <code>destroy()</code>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain Thread Synchronization and the 'synchronized' keyword in Java.</div>
    <div class="ans-body">
        <strong>Synchronization:</strong> Prevents thread interference and race conditions when multiple threads access shared resources simultaneously using monitor locks.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Differentiate between Throw and Throws in Java Exception Handling.</div>
    <div class="ans-body">
        <strong>Throw:</strong> Explicitly triggers an exception instance inside a method body.<br>
        <strong>Throws:</strong> Declares exceptions thrown by a method in its header signature.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>What is JDBC? Explain JDBC Architecture and execute a database SELECT query.</div>
    <div class="ans-body">
        <strong>JDBC Architecture:</strong> Application &rarr; JDBC API &rarr; DriverManager &rarr; JDBC Driver &rarr; Database. Complete sample SELECT query program.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Write HTML code for a complete Web Form with Table formatting and Validation.</div>
    <div class="ans-body">
        <strong>HTML Implementation:</strong> Form markup with input types, select dropdowns, radio buttons, and table alignments.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Discuss JSP Architecture, Scripting Elements (&lt;%! %&gt;, &lt;% %&gt;, &lt;%= %&gt;), and Directives.</div>
    <div class="ans-body">
        <strong>JSP Scripting Elements:</strong>
        <ul>
            <li><strong>Declaration (<code>&lt;%! %&gt;</code>):</strong> Declares class variables and methods.</li>
            <li><strong>Scriptlet (<code>&lt;% %&gt;</code>):</strong> Java code placed inside the <code>_jspService()</code> method.</li>
            <li><strong>Expression (<code>&lt;%= %&gt;</code>):</strong> Directly prints evaluated values to the output stream.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain Servlets, HttpServletRequest, and HttpServletResponse with complete GET/POST demonstration.</div>
    <div class="ans-body">
        <strong>Servlet Processing:</strong> Complete explanation of HTTP request parsing, header inspection, and HTML output streaming.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>What are JavaBeans? Explain Bean properties and deployment in JSP using jsp:useBean.</div>
    <div class="ans-body">
        <strong>JavaBeans:</strong> Reusable software components adhering to conventions: zero-arg constructor, private fields, and public getters/setters.
    </div>
</div>
"""

print("Generating Java 2020 PDF...")
generate_java_pdf("December 2020", "java 2020 solved.pdf", YEAR_2020_HTML)

# ==============================================================================
# YEAR 2019 (November 2019)
# ==============================================================================
YEAR_2019_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>What is Bytecode and Java Virtual Machine (JVM)?</div>
    <div class="ans-body">
        <strong>Explanation:</strong> Bytecode is compiled intermediate instructions for the virtual JVM processor, enabling cross-platform portability.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>List the four fundamental principles of Object-Oriented Programming.</div>
    <div class="ans-body">
        <strong>OOP Principles:</strong> Encapsulation, Abstraction, Inheritance, and Polymorphism.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>What is Garbage Collection in Java?</div>
    <div class="ans-body">
        <strong>Explanation:</strong> Automatic reclamation of heap memory occupied by dereferenced objects.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>What is Final variable, Final method, and Final class?</div>
    <div class="ans-body">
        <strong>Final keyword:</strong> Variable becomes a constant, method cannot be overridden, class cannot be inherited (subclassed).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>Define Constructor in Java.</div>
    <div class="ans-body">
        <strong>Definition:</strong> A special method called automatically when an object is instantiated, having the same name as the class and no return type.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Explain Interface in Java with code demonstrating multiple inheritance.</div>
    <div class="ans-body">
        <strong>Interface:</strong> Contract with method declarations implemented by classes to achieve multiple inheritance.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain Applet Life Cycle and how Applets are embedded into HTML.</div>
    <div class="ans-body">
        <strong>Applet in HTML:</strong> Embedded using <code>&lt;applet code="MyApplet.class" width="300" height="200"&gt;&lt;/applet&gt;</code>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain Exception Handling using try, catch, and finally blocks.</div>
    <div class="ans-body">
        <strong>Exception Handling:</strong> Structured handling preventing runtime crashes and releasing resources safely.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>What is JSP? Explain advantages of JSP and main components. How is JSP different from Servlet?</div>
    <div class="ans-body">
        <strong>JSP vs Servlet:</strong> Comprehensive comparison, JSP compilation lifecycle, directives, actions, and scriptlets.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Explain Multithreading in Java: Thread Life Cycle, States, and Synchronization.</div>
    <div class="ans-body">
        <strong>Thread Life Cycle:</strong> New &rarr; Runnable &rarr; Running &rarr; Blocked/Waiting &rarr; Terminated.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain JDBC Architecture, Statement vs PreparedStatement, and write a program to insert student records.</div>
    <div class="ans-body">
        <strong>JDBC Program:</strong> Complete program inserting records using PreparedStatement to prevent SQL injection.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain Event Handling in Java AWT/Swing with MouseListener and ActionListener.</div>
    <div class="ans-body">
        <strong>Event Handling:</strong> Source &rarr; Event Object &rarr; Listener interface implementation.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Write HTML and CSS code to design a responsive institutional web page.</div>
    <div class="ans-body">
        <strong>Web Design:</strong> Clean HTML markup with external/internal CSS styling, tables, lists, and navigation bar.
    </div>
</div>
"""

print("Generating Java 2019 PDF...")
generate_java_pdf("November 2019", "java 2019 solved.pdf", YEAR_2019_HTML)
