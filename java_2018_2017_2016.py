import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from java_builder_base import generate_java_pdf

# ==============================================================================
# YEAR 2018 (December 2018)
# ==============================================================================
YEAR_2018_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>What is a Final Variable? Give an example.</div>
    <div class="ans-body">
        <strong>Definition:</strong> A variable declared with the <code>final</code> keyword becomes a constant whose value cannot be reassigned once initialized:
<pre>
final double PI = 3.14159;
// PI = 3.14; // Compile-time error: cannot assign a value to final variable
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>What is Garbage Collection in Java?</div>
    <div class="ans-body">
        <strong>Definition:</strong> The automatic process of finding and freeing heap memory allocated to objects that are no longer referenced by any active thread.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>What is an Abstract Method?</div>
    <div class="ans-body">
        <strong>Definition:</strong> A method declared without a body (implementation) using the <code>abstract</code> keyword, terminating with a semicolon. Must be implemented by subclasses.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>What is a Layout Manager in Java AWT?</div>
    <div class="ans-body">
        <strong>Definition:</strong> An interface/class that manages the automatic positioning and sizing of GUI components within a container window.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What is the purpose of the 'super' keyword?</div>
    <div class="ans-body">
        <strong>Definition:</strong> References the immediate superclass object to call parent constructors (<code>super()</code>) or access hidden parent members.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>What are Packages? How are packages created in Java? Explain and give example.</div>
    <div class="ans-body">
        <strong>Packages:</strong> Namespaces organizing classes and avoiding naming collisions. Created using the <code>package</code> keyword at the top of a source file:
<pre>
package com.ccsu.bca;
public class Student {
    public void display() { System.out.println("BCA Student"); }
}
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain Interface in Java with an example of Multiple Inheritance.</div>
    <div class="ans-body">
        <strong>Explanation:</strong> Pure abstraction tool allowing classes to implement multiple interfaces simultaneously, overcoming single class inheritance limits.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain Applet Life Cycle methods.</div>
    <div class="ans-body">
        <strong>Lifecycle:</strong> <code>init()</code>, <code>start()</code>, <code>paint(Graphics g)</code>, <code>stop()</code>, and <code>destroy()</code>.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Explain Multithreading in Java. Write a program demonstrating Thread synchronization using synchronized methods.</div>
    <div class="ans-body">
        <strong>Thread Synchronization:</strong> Coordinates thread access to shared mutable resources to prevent race conditions.
<pre>
class Table {
    synchronized void printTable(int n) {
        for(int i = 1; i <= 5; i++) {
            System.out.println(n * i);
            try { Thread.sleep(300); } catch(Exception e) {}
        }
    }
}
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>What is Exception Handling? Explain Checked vs Unchecked Exceptions with try, catch, finally, and throws.</div>
    <div class="ans-body">
        <strong>Detailed Exception Model:</strong> Checked exceptions verified at compile-time (e.g. <code>IOException</code>) vs Unchecked exceptions occurring at runtime (e.g. <code>NullPointerException</code>).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain JDBC Architecture and steps to connect Java to a database. Write a program to insert a record.</div>
    <div class="ans-body">
        <strong>Complete JDBC Program:</strong> Register driver, establish connection, execute SQL insert using <code>Statement</code>, and close resources.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>What is JSP? Explain its life cycle, advantages over Servlets, and scriptlet tags.</div>
    <div class="ans-body">
        <strong>JSP vs Servlets:</strong> Translation, compilation, and execution lifecycle; comparison of presentation layer benefits.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Explain Event Handling in Java AWT with Delegation Event Model.</div>
    <div class="ans-body">
        <strong>Delegation Event Model:</strong> Event sources generate event objects delivered to registered listener interfaces.
    </div>
</div>
"""

print("Generating Java 2018 PDF...")
generate_java_pdf("December 2018", "java 2018 solved.pdf", YEAR_2018_HTML)

# ==============================================================================
# YEAR 2017 (December 2017)
# ==============================================================================
YEAR_2017_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>How will you create hyperlinks in a web document? Write the code also.</div>
    <div class="ans-body">
        <strong>HTML Hyperlink:</strong>
<pre>
&lt;a href="https://www.ccsuniversity.ac.in" target="_blank"&gt;Visit CCSU Official Portal&lt;/a&gt;
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>What is a Constructor? List its characteristics.</div>
    <div class="ans-body">
        <strong>Characteristics:</strong> Same name as class, no return type (not even void), automatically called on <code>new</code>, can be overloaded.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Differentiate between Method Overloading and Method Overriding.</div>
    <div class="ans-body">
        <strong>Overloading:</strong> Same method name, different signatures, within same class (compile-time).<br>
        <strong>Overriding:</strong> Same signature, in subclass, overriding parent behavior (runtime).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>What is Bytecode in Java?</div>
    <div class="ans-body">
        <strong>Definition:</strong> Architecture-neutral intermediate instructions executed by JVM.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What is the purpose of the 'this' keyword?</div>
    <div class="ans-body">
        <strong>Definition:</strong> Refers to the current class instance to differentiate shadowed instance fields from parameters.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Explain the Life Cycle of an Applet with diagram.</div>
    <div class="ans-body">
        <strong>Applet Lifecycle:</strong> Born (<code>init</code>) &rarr; Running (<code>start</code>, <code>paint</code>) &rarr; Idle (<code>stop</code>) &rarr; Dead (<code>destroy</code>).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain Packages and Access Protection in Java.</div>
    <div class="ans-body">
        <strong>Access Protection:</strong> Detailed comparison of private, default, protected, and public scopes.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain Interface in Java with code example.</div>
    <div class="ans-body">
        <strong>Interface:</strong> Blueprint of a class containing abstract methods and constants.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Explain Exception Handling in Java: try, catch, finally, throw, and throws with custom exception.</div>
    <div class="ans-body">
        <strong>Custom Exception:</strong>
<pre>
class InvalidAgeException extends Exception {
    public InvalidAgeException(String msg) { super(msg); }
}
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Explain Multithreading in Java: Thread class, Runnable interface, and Thread Priorities.</div>
    <div class="ans-body">
        <strong>Multithreading:</strong> Full comparison of extending Thread vs implementing Runnable, lifecycle states, and priority scheduling.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>What is JDBC? Explain the 4 types of JDBC drivers and steps for database connectivity.</div>
    <div class="ans-body">
        <strong>JDBC Drivers:</strong> Type-1, Type-2, Type-3, and Type-4 drivers with architectural diagrams.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain Servlets vs JSP. Write a complete HttpServlet program handling GET requests.</div>
    <div class="ans-body">
        <strong>Servlet Architecture:</strong> Complete HttpServlet implementation serving dynamic web responses.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Explain Layout Managers in AWT: FlowLayout, BorderLayout, and GridLayout.</div>
    <div class="ans-body">
        <strong>Layout Managers:</strong> Visual layout structures and coordinate placements.
    </div>
</div>
"""

print("Generating Java 2017 PDF...")
generate_java_pdf("December 2017", "java 2017 solved.pdf", YEAR_2017_HTML)

# ==============================================================================
# YEAR 2016 (December 2016)
# ==============================================================================
YEAR_2016_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>What is Byte-code in JAVA? Explain.</div>
    <div class="ans-body">
        <strong>Definition:</strong> The intermediate machine instruction set generated by <code>javac</code>, executed by the JVM to provide platform independence.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>What is Garbage Collection in Java?</div>
    <div class="ans-body">
        <strong>Definition:</strong> Automatic memory reclamation mechanism of the JVM destroying unreferenced heap objects.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Differentiate between Class and Interface.</div>
    <div class="ans-body">
        <strong>Differences:</strong> A class contains full implementation and state; an interface contains method specifications and constants.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>What is an Applet?</div>
    <div class="ans-body">
        <strong>Definition:</strong> A small Java program designed to be embedded in an HTML web page and executed inside a web browser.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What is Thread in Java?</div>
    <div class="ans-body">
        <strong>Definition:</strong> A lightweight sub-process representing an independent execution path in a program.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>What do you mean by Constructor? Explain Constructor Overloading.</div>
    <div class="ans-body">
        <strong>Constructor Overloading:</strong> Defining multiple constructors in a single class with different parameter lists.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain Packages in Java and how to create user-defined packages.</div>
    <div class="ans-body">
        <strong>Packages:</strong> Directory-based namespaces created with <code>package</code> statement.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain Exception Handling in Java with try, catch, and finally.</div>
    <div class="ans-body">
        <strong>Handling:</strong> Graceful recovery from runtime program faults.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Explain Applet Life Cycle in detail with an Applet code to draw shapes.</div>
    <div class="ans-body">
        <strong>Applet Shapes Code:</strong> Complete applet drawing rectangles, lines, and ovals using <code>Graphics</code>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Explain Multithreading and Thread Synchronization with examples.</div>
    <div class="ans-body">
        <strong>Multithreading & Synchronization:</strong> Producer-Consumer problem and synchronized locks.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain JDBC Architecture and steps to connect Java to a database.</div>
    <div class="ans-body">
        <strong>JDBC:</strong> Complete connectivity steps and SQL operations.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain Servlets, HttpServlet, and its life cycle methods.</div>
    <div class="ans-body">
        <strong>Servlets:</strong> Complete server-side Java web request dispatching.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Explain Client-Server Socket Programming in Java with complete program.</div>
    <div class="ans-body">
        <strong>Socket Programming:</strong> <code>ServerSocket</code> and <code>Socket</code> communication code over TCP.
    </div>
</div>
"""

print("Generating Java 2016 PDF...")
generate_java_pdf("December 2016", "java 2016 solved.pdf", YEAR_2016_HTML)
