# even_odd_string_splitter
# Even Odd String Splitter

## 📌 Problem

Given a string **S**, print its even-indexed and odd-indexed characters as space-separated strings.

* Index `0` is considered even.
* Handle multiple test cases.

---

## 🧠 Approach

* Traverse the string
* Extract:

  * Even-index characters → `s[::2]`
  * Odd-index characters → `s[1::2]`

---

## 🚀 Input Format

* First line: Integer `T` (number of test cases)
* Next `T` lines: Each contains a string

---

## 📤 Output Format

* For each test case:
```
<even-indexed chars> <odd-indexed chars>
```

## 💻 Example

### Input
```
2
Hacker
Rank
```

### Output
```
Hce akr
Rn ak
```
