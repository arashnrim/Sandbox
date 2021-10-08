/*
    Hello, Rust!
    This file aims to explore the Rust programming language. Just to play around, of course, and 
    have a simple compiled list of the syntax of Rust!
*/

/*
    The main() function is the main entry point of every Rust program; this shouldn't be too
    surprising since many programming languages do this too.
*/
fn main() {
    example_function();
    hello_world();
    constants_and_variables();
}

// ===================
// FUNCTIONS
// ===================

/*
    Declaring a function is as simple as using the `fn` keyword followed by the name of the
    function.
    
    Interestingly, the compiler warns you if your function name is non-snake case. I assume
    that the de facto standard of Rust function names is the snake case convention!
 */
fn example_function() {
    // Enter code here
}

fn hello_world() {
    /*
        println!() is the equivalent of outputting content. Since you're familiar with 
        Python, it's the equivalent of Python's print() command!
    */
    println!("Hello, world!");
}

fn constants_and_variables() {
    /*
        In Rust, both constants and variables are defined with the `let` keyword. A little
        similar to Swift, but different later on.

        Alternatively, the `const` keyword can be used to define a constant. However, the
        type of the constant must be explicitly mentioned and the constant is strictly
        immutable.
     */
    let language_name = "Rust";
    const LANGUAGE_MASCOT: &str = "Ferris";

    /*
        language_name = ""; <- ⚠ error
        languge_mascot = "Gopher"; <- ⚠ error

        Rust will raise an error when you attempt to change the value of a constant. Constants
        are immutable, and hence their values cannot be changed.
    */

    println!("language_name: {}", language_name);
    println!("language_mascot: {}", LANGUAGE_MASCOT);

    /*
        On the other hand, variables are defined with the `let mut` keywords. As probably
        guessable, the `mut` here stands for mutable; the value of mutable variables can change.
    */
    let mut greeting = "Good morning!";
    println!("greeting (at declaration): {}", greeting);

    greeting = "Good afternoon!";
    println!("greeting (after reassignment): {}", greeting);
}