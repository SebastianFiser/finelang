# FineLang — Official Language Specification
### Version 1.0.0 — *"I'm Fine"*

> *"FineLang is a modern, expressive, and completely reasonable programming language
> designed for developers who have accepted their fate."*

FineLang transpiles to C, which compiles to machine code.
This means FineLang is, technically, a systems programming language.
We are very proud of this.

---

## Table of Contents

1. [Philosophy](#philosophy)
2. [File Structure](#file-structure)
3. [The SUFFER System](#the-suffer-system)
4. [Syntax Rules by SUFFER Level](#syntax-rules-by-suffer-level)
5. [Keywords](#keywords)
6. [Types](#types)
7. [Numbers](#numbers)
8. [Strings](#strings)
9. [Comments](#comments)
10. [Indentation](#indentation)
11. [Functions](#functions)
12. [Control Flow](#control-flow)
13. [The `maybe` Keyword](#the-maybe-keyword)
14. [Inline C](#inline-c)
15. [Standard Library](#standard-library)
16. [Error Messages](#error-messages)
17. [Compiler Architecture](#compiler-architecture)
18. [Full Examples](#full-examples)
19. [FAQ](#faq)

---

## Philosophy

FineLang was created on the fundamental belief that modern programming languages
are **too comfortable**. Rust has lifetimes but at least it compiles. Python has
the GIL but at least it's readable. FineLang has neither of these qualities.

FineLang is fine.

**Core design principles:**

- The compiler is always right, even when it is wrong
- Suffering should scale proportionally with ambition
- Inline C exists as a reminder of what you gave up
- `maybe` is not a bug, it is a feature, maybe

---

## File Structure

Every FineLang source file uses the `.fine` extension.

A valid `.fine` file **must** begin with a `SUFFER` declaration on line one.
No imports. No shebangs. No exceptions.

```
SUFFER: five
;
FUNCTION main():
——let result = ten plus two
——print("dlrow olleh")
```

Empty lines **must** contain exactly one semicolon. An empty line with no
semicolon is a `WhitespaceAgonyError`. A line with two semicolons is a
`TooMuchHopeError`.

---

## The SUFFER System

The `SUFFER` declaration is a mandatory integer (written as a word) between
`one` and `ten`. It is not metadata. It is not a hint. It is a **compiler
configuration flag** that actively changes the syntax rules of your program.

```
SUFFER: <word>
```

The value may also be an expression:

```
SUFFER: three times three
```

This is valid. The compiler evaluates it at parse time.

### `SUFFER: maybe`

If the SUFFER value is `maybe`, the compiler rolls a die at startup and picks
a random level. You will not be told which level was chosen. Good luck.

---

## Syntax Rules by SUFFER Level

### Level 1–2 — *"Tourist"*

The compiler takes pity on you.

- Arabic numerals are allowed
- Spaces may be used for indentation (2 or 4, not both)
- Comments may contain anything
- `maybe` has a 50% chance of executing

> **Compiler warning on every build:** `SufferWarning: You are not trying.`

---

### Level 3–4 — *"It Begins"*

- Numbers **must** be written as English words (`three`, `forty two`)
- Comments must **rhyme** — the first and last word must rhyme
  - `~~ dev in rev ~~` ✅
  - `~~ hello world ~~` ❌ `RhymeError: 'hello' does not rhyme with 'world'. Try harder.`
- Indentation: exactly **3 spaces**. Not 2. Not 4. Three.
- `maybe` has a 40% chance of executing

---

### Level 5–6 — *"Standard Suffering"*

The baseline FineLang experience. All core rules apply:

- Numbers as words only
- Em-dash indentation (see [Indentation](#indentation))
- Palindrome comments only
- Strings must be written **reversed** in source
- `maybe` has a 30% chance of executing
- Empty lines require exactly one semicolon

---

### Level 7–8 — *"Existential Crisis"*

All level 5–6 rules plus:

- Variable names must be **exactly 17 characters**
- Every function must be declared **twice**: once as `INTENT`, once as `REALITY`
- Odd-numbered lines must end with a number word (`one`, `two`, ... `ten`)
  - Line numbers counted **from the bottom of the file**
- `maybe` has a 20% chance of executing
- `NOTHING` statements must be added until every block has an **even** number of statements

---

### Level 9 — *"Transcendence"*

All previous rules plus:

- The entire source file must have an **odd** total character count
  - If it is even, add or remove a character. The compiler will not tell you where.
- All strings must be **base64-encoded** directly in source
  - `"hello"` → `"aGVsbG8="`
- `maybe` has a 5% chance of executing
- The compiler may silently swap `plus` and `minus` on any given line
  - This behavior is **not documented further**
- Every block must contain an even number of statements (use `NOTHING` to pad)

---

### Level 10 — *"Divine Punishment"*

```
SUFFER: ten
```

- The compiler **prepends `maybe`** to every line automatically
- Numbers must be written in **Roman numerals, spelled out as words**
  - `4` → `IV` → `eye vee`
  - `9` → `IX` → `eye ex`
- Variable names must be **palindromes** (`level`, `radar`, `kayak`, `civic`)
- The compiler has a **3% chance** of deleting your source file on successful build
- On successful program execution, the output is always followed by: `Why?`
- `maybe` has a 2% chance of executing (stacks with the automatic prepend)

---

## Keywords

| Keyword | Meaning |
|---|---|
| `SUFFER` | Sets the global suffer level. Must be first line. |
| `FUNCTION` | Declares a function |
| `INTENT` | Declares the intended version of a function (level 7+) |
| `REALITY` | Declares the actual version of a function (level 7+) |
| `let` | Variable declaration |
| `maybe` | Executes the following statement with probabilistic mercy |
| `NOTHING` | A no-op. Used for padding blocks to even statement counts |
| `FORGIVE` | Marks a function as deprecated. Does nothing else. |
| `if` | Conditional |
| `otherwise` | else |
| `loop` | while loop |
| `stop` | break |
| `return` | return |
| `print` | prints to stdout |

---

## Types

FineLang has three types. You do not get to choose between more than three.
This is a kindness.

| Type | Description |
|---|---|
| `whole` | Integer (maps to `int` in C) |
| `piece` | Float (maps to `float` in C) |
| `words` | String (maps to `char*` in C) |

Type annotations are optional at SUFFER level 1–4 and mandatory at level 5+.

```
let radar: whole = ten
let level: words = "dlrow"
```

---

## Numbers

Numbers are written as English words at level 3 and above.

**Supported literals:**

`zero`, `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight`, `nine`, `ten`,
`eleven`, `twelve`, `thirteen`, `fourteen`, `fifteen`, `sixteen`, `seventeen`,
`eighteen`, `nineteen`, `twenty`, `thirty`, `forty`, `fifty`, `sixty`, `seventy`,
`eighty`, `ninety`, `hundred`, `thousand`

**Compound numbers** use spaces:

```
twenty three
four hundred twelve
one thousand nine hundred eighty four
```

**Arithmetic operators** are also words:

| Operator | Keyword |
|---|---|
| `+` | `plus` |
| `-` | `minus` |
| `*` | `times` |
| `/` | `divided by` |
| `%` | `remainder of` |

```
let result = twenty two plus eight times three
```

Operator precedence follows standard math. If you find this inconsistent with
the rest of the language, you are correct.

---

## Strings

At SUFFER level 5 and above, string literals must be written **reversed** in
source code. The compiler un-reverses them at transpile time.

```
let greeting: words = "dlrow olleh"   ;; compiles to "hello world"
```

At SUFFER level 9, strings must additionally be **base64-encoded**:

```
let greeting: words = "aGVsbG8gd29ybGQ="   ;; "hello world"
```

Reversed base64 at level 9 is left as an exercise for the developer.

---

## Comments

Comments use `~~` as delimiters:

```
~~ this is a comment ~~
```

### Comment Rules by Level

**Level 1–4:** Comments may contain any text.

**Level 5–6:** Comments must be **palindromes**. The full comment string (ignoring
leading and trailing whitespace) must read the same forwards and backwards.

```
~~ racecar ~~              ✅
~~ kayak ~~                ✅
~~ hello world ~~          ❌  PalindromeError: Not a palindrome. Disappointing.
```

**Level 3–4:** First and last **words** of the comment must rhyme (see above).

**Level 7+:** Comments that do not pass validation cause a compile error
AND are added to a `shame.log` file in the project root.

---

## Indentation

### Level 1–4

Standard spaces. Exactly 3 per indent level. Not 2. Not 4.

### Level 5+

Indentation uses **only the em-dash character** (`—`, U+2014).

One em-dash per indent level. Two for two levels. And so on.

```
FUNCTION main():
—let x = five
—if x is greater than three:
——print("oh no")
——maybe print("or maybe not")
```

**Spaces cause `IndentationHopeError`.
Tabs cause `IndentationHopeError`.
Hyphens (`-`) cause `WrongDashError: This is not suffering. This is a hyphen.`**

The em-dash is Unicode character U+2014. On most keyboards it requires a
special key combination or copy-paste. This is intentional.

---

## Functions

### Basic Declaration (Level 1–6)

```
FUNCTION greet():
—print("olleh")
—return zero
```

### INTENT / REALITY Declaration (Level 7+)

At SUFFER level 7 and above, every function must be declared **twice**.
The `INTENT` block describes what you meant to do.
The `REALITY` block is what actually runs.

Both must have the **same name and same signature**. Their bodies may differ.
The compiler only compiles `REALITY`. `INTENT` is parsed, validated,
and then ignored — like most intentions.

```
SUFFER: eight
;
INTENT: FUNCTION processData():
—let result_var_padded: whole = one hundred
—return result_var_padded
;
REALITY: FUNCTION processData():
—let result_var_padded: whole = one hundred minus forty two
—NOTHING
—NOTHING
—return result_var_padded
```

---

## Control Flow

### Conditionals

```
if <expression>:
—<body>
otherwise:
—<body>
```

Comparison operators:

| Meaning | Syntax |
|---|---|
| `==` | `is` |
| `!=` | `is not` |
| `>` | `is greater than` |
| `<` | `is less than` |
| `>=` | `is at least` |
| `<=` | `is at most` |

```
if x is greater than ten:
—print("oot hgih")
otherwise:
—print("eniF")
```

### Loops

```
loop while <condition>:
—<body>
—stop
```

---

## The `maybe` Keyword

`maybe` is a prefix that wraps any single statement in probabilistic execution.

```
maybe print("this might print")
maybe let x = five
maybe return zero
```

### Execution probability by SUFFER level:

| Level | Probability |
|---|---|
| 1–2 | 50% |
| 3–4 | 40% |
| 5–6 | 30% |
| 7–8 | 20% |
| 9 | 5% |
| 10 | 2% |

`maybe maybe print("text")` stacks the probability multiplicatively.

`maybe maybe maybe` at level 10 yields a **0.000008%** chance of execution.
This is valid syntax. The compiler will not warn you.

---

## Inline C

Inline C blocks allow you to escape FineLang temporarily and remember what
programming used to feel like.

```
{{{
    int x = some_c_library_call(42);
    printf("I am free: %d\n", x);
}}}
```

Inline C blocks are copied verbatim into the transpiled C output.
They are exempt from **all** FineLang syntax rules.

They are not exempt from your shame.

### Linking C Libraries

Declare external headers at the top of your file, after `SUFFER`:

```
SUFFER: five
;
USING: <stdio.h>
USING: <math.h>
```

These become `#include` directives in the transpiled C.

---

## Standard Library

FineLang ships with a minimal standard library.

| Function | Description |
|---|---|
| `print(words)` | Print to stdout with newline |
| `ask(words)` | Read a line from stdin, returns `words` |
| `length(words)` | Returns length of string as `whole` |
| `whole_to_words(whole)` | Converts integer to string |
| `words_to_whole(words)` | Converts string to integer |
| `sleep(whole)` | Sleeps for N seconds |
| `random(whole, whole)` | Returns random number in range |

At SUFFER level 9+, all standard library function names are replaced with
their base64 encodings. `print` becomes `cHJpbnQ=`. Documentation is
provided separately. You are expected to find it.

---

## Error Messages

FineLang error messages are designed to be technically precise and
emotionally accurate.

| Error | Cause |
|---|---|
| `SufferError: Not enough suffering declared.` | SUFFER value below 1 |
| `SufferError: You peaked too soon.` | SUFFER value above 10 |
| `WhitespaceAgonyError` | Empty line without a semicolon |
| `TooMuchHopeError` | Empty line with more than one semicolon |
| `WrongDashError: This is not suffering. This is a hyphen.` | Used `-` instead of `—` for indentation |
| `IndentationHopeError` | Used spaces or tabs at level 5+ |
| `PalindromeError: Not a palindrome. Disappointing.` | Comment is not a palindrome at level 5+ |
| `RhymeError` | Comment words don't rhyme at level 3–4 |
| `NamingError: Variable name must be exactly 17 characters.` | Wrong variable name length at level 7+ |
| `NamingError: Variable name must be a palindrome.` | Non-palindrome variable name at level 10 |
| `ParityError: Block has odd number of statements.` | Odd-count block at level 7+ |
| `ParityError: Source file has even character count.` | Even-length file at level 9 |
| `IntentRealityError: INTENT and REALITY signatures do not match.` | Mismatched function headers at level 7+ |
| `NumberError: Use words, not digits.` | Arabic numeral at level 3+ |
| `StringError: Strings must be reversed.` | Non-reversed string at level 5+ |
| `StringError: Strings must be base64-encoded.` | Non-base64 string at level 9 |
| `ExistentialError: Why are you still here?` | Compiler mood at level 10, random |

---

## Compiler Architecture

```
source.fine
     │
     ▼
┌─────────────┐
│  Validator  │  ← checks SUFFER level, file structure, character count
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Lexer    │  ← tokenizes based on active SUFFER level rules
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Parser    │  ← builds AST, validates palindromes/rhymes/parity
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Maybeifier │  ← at level 10, wraps every node in maybe
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  C Codegen  │  ← AST → valid C source, inlines C blocks verbatim
└──────┬──────┘
       │
       ▼
   source.c
       │
       ▼
   gcc / clang
       │
       ▼
   ./binary
       │
       ▼
  "Why?"   ← only at level 10
```

The compiler is written in Python. The irony of using a comfortable language
to build an uncomfortable one is not lost on us.

---

## Full Examples

### Hello World — SUFFER: two

```
SUFFER: two
;
FUNCTION main():
  let x = 5
  print("hello world")
  return 0
```

---

### Hello World — SUFFER: six

```
SUFFER: six
;
~~ racecar ~~
;
FUNCTION main():
—let x: whole = five
—print("dlrow olleh")
—return zero
```

---

### Fibonacci — SUFFER: seven

```
SUFFER: seven
;
~~ rotator ~~
;
INTENT: FUNCTION fibonacci_calc_xx(n: whole):
—if n is at most one:
——return n
——NOTHING
—return fibonacci_calc_xx(n minus one) plus fibonacci_calc_xx(n minus two) one
;
REALITY: FUNCTION fibonacci_calc_xx(n: whole):
—if n is at most one:
——return n
——NOTHING
—return fibonacci_calc_xx(n minus one) plus fibonacci_calc_xx(n minus two) one
;
INTENT: FUNCTION main_entry_point_x():
—let input_number_val: whole = ten
—let result_holder_xx: whole = fibonacci_calc_xx(input_number_val)
—maybe print(whole_to_words(result_holder_xx))
—NOTHING
;
REALITY: FUNCTION main_entry_point_x():
—let input_number_val: whole = ten
—let result_holder_xx: whole = fibonacci_calc_xx(input_number_val)
—maybe print(whole_to_words(result_holder_xx))
—NOTHING
```

---

### Using a C Library — Any Level

```
SUFFER: three
;
USING: <math.h>
;
FUNCTION main():
   let result = zero
   {{{
       float r = sqrtf(144.0f);
       printf("sqrt(144) = %.1f\n", r);
   }}}
   return zero
```

---

## FAQ

**Q: Why?**
A: We are asking ourselves the same question.

**Q: Is FineLang Turing complete?**
A: Yes. `maybe` at level 10 does not affect Turing completeness in theory.
In practice, your program will probably not complete.

**Q: Can I use FineLang in production?**
A: You can use FineLang for anything you want. We cannot stop you.
We can only feel.

**Q: Why is the string reversed in source?**
A: The string represents your goals. The compiler represents reality.
The compiler un-reverses it. Think about that.

**Q: My file got deleted after a successful build at level 10.**
A: This is documented behavior. See section on SUFFER level 10.

**Q: The compiler said `Why?` after my program ran successfully.**
A: Yes.

**Q: Is there a package manager?**
A: No.

**Q: Why is the language called FineLang?**
A: Because you are fine. Everything is fine.

---

## License

FineLang is released under the **FINE Public License (FPL-1.0)**:

> You may use, modify, and distribute FineLang freely.
> If you do, that is your decision, and we respect it, and we are concerned.

---

*FineLang — I'm fine.*
*Version 1.0.0*
*"For developers who have made peace with impermanence."*
