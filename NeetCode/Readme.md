# 🚀 My NeetCode 150 Journey: The 30-Day Sprint

> "Amateurs sit and wait for inspiration, the rest of us just get up and go to work."

Welcome to my customized NeetCode 150 tracker! I am executing a highly condensed 30-day schedule. Because I reserve Mondays strictly for Revision/Testing and take Tuesdays off, I am tackling **6-7 new problems** on my active coding days.

## 📊 Progress Tracker (Based on Custom UI)
* **Goal:** 150 Problems in 30 Days
* **Starting Progress:** 6 / 150 Solved 
* **Pace:** ~6.5 problems per active coding day.

---

## 🗓️ The 30-Day Battle Plan


### Week 1: Arrays, Pointers & Stack (Days 1–7)
| Day | Type | Focus Topics | Problem Count |
| :--- | :--- | :--- | :--- |
| **Day 1 (Wed)** | 💻 Code | Arrays & Hashing (Finish last 5) + Two Pointers (1) | 6 |
| **Day 2 (Thu)** | 💻 Code | Two Pointers (Finish last 4) + Sliding Window (2) | 6 |
| **Day 3 (Fri)** | 💻 Code | Sliding Window (Finish last 4) + Stack (3) | 7 |
| **Day 4 (Sat)** | 💻 Code | Stack (Finish last 3) + Binary Search (4) | 7 |
| **Day 5 (Sun)** | 💻 Code | Binary Search (Finish last 3) + Linked List (4) | 7 |
| **Day 6 (Mon)** | 🧠 Review | **WEEKLY MONDAY REVISION TEST** | 0 |
| **Day 7 (Tue)** | 🛑 Rest | *No Contribution / Rest Day* | 0 |

### Week 2: Linked Lists, Trees & Heaps (Days 8–14)
| Day | Type | Focus Topics | Problem Count |
| :--- | :--- | :--- | :--- |
| **Day 8 (Wed)** | 💻 Code | Linked List (Finish last 7) | 7 |
| **Day 9 (Thu)** | 💻 Code | Trees (First 7 of 15) | 7 |
| **Day 10 (Fri)** | 💻 Code | Trees (Finish last 8) | 8 |
| **Day 11 (Sat)** | 💻 Code | Heap / Priority Queue (All 7) | 7 |
| **Day 12 (Sun)** | 💻 Code | Backtracking (First 7 of 10) | 7 |
| **Day 13 (Mon)** | 🧠 Review | **WEEKLY MONDAY REVISION TEST** | 0 |
| **Day 14 (Tue)** | 🛑 Rest | *No Contribution / Rest Day* | 0 |

### Week 3: Graphs & Dynamic Programming (Days 15–21)
| Day | Type | Focus Topics | Problem Count |
| :--- | :--- | :--- | :--- |
| **Day 15 (Wed)** | 💻 Code | Backtracking (Finish 3) + Tries (All 3) + Graphs (1) | 7 |
| **Day 16 (Thu)** | 💻 Code | Graphs (Next 7) | 7 |
| **Day 17 (Fri)** | 💻 Code | Graphs (Finish last 5) + Advanced Graphs (2) | 7 |
| **Day 18 (Sat)** | 💻 Code | Advanced Graphs (Finish 4) + 1-D DP (First 3) | 7 |
| **Day 19 (Sun)** | 💻 Code | 1-D DP (Next 7) | 7 |
| **Day 20 (Mon)** | 🧠 Review | **WEEKLY MONDAY REVISION TEST** | 0 |
| **Day 21 (Tue)** | 🛑 Rest | *No Contribution / Rest Day* | 0 |

### Week 4: Deep DP, Greedy & Intervals (Days 22–28)
| Day | Type | Focus Topics | Problem Count |
| :--- | :--- | :--- | :--- |
| **Day 22 (Wed)** | 💻 Code | 1-D DP (Finish last 1) + 2-D DP (First 6) | 7 |
| **Day 23 (Thu)** | 💻 Code | 2-D DP (Finish last 5) + Greedy (First 2) | 7 |
| **Day 24 (Fri)** | 💻 Code | Greedy (Finish last 6) + Intervals (First 1) | 7 |
| **Day 25 (Sat)** | 💻 Code | Intervals (Finish last 5) + Math & Geometry (2) | 7 |
| **Day 26 (Sun)** | 💻 Code | Math & Geometry (Finish last 6) | 6 |
| **Day 27 (Mon)** | 🧠 Review | **WEEKLY MONDAY REVISION TEST** | 0 |
| **Day 28 (Tue)** | 🛑 Rest | *No Contribution / Rest Day* | 0 |

### Week 5: The Final Stretch (Days 29–30)
| Day | Type | Focus Topics | Problem Count |
| :--- | :--- | :--- | :--- |
| **Day 29 (Wed)** | 💻 Code | Bit Manipulation (Finish remaining 6) | 6 |
| **Day 30 (Thu)** | 🏆 Finish| Buffer Day: Catch up on any problems missed! | Var. |

---




# 🕵️‍♂️ The LeetCode Pattern Cheat Sheet

A quick-reference guide to translating interview prompts into actionable algorithms.

---

## 1. The "Sliding Window" Pattern
* **The Hidden Clues:** "Contiguous", "Subarray", "Substring", "Longest", "Shortest", "Maximum/Minimum".
* **The Translation:** The word **"Contiguous"** (or subarray/substring) is the ultimate giveaway. It means the items must be sitting right next to each other. Whenever you need to find the "best" chunk of items sitting next to each other, use a sliding window.
> ⚠️ **The Trap:** If the prompt says "Subsequence" or "Subset", you **cannot** use a sliding window, because subsequences don't have to be next to each other.

## 2. The "Two Pointers" Pattern
* **The Hidden Clues:** "Sorted array", "Pairs", "Palindromes", "Sum to a target" (when sorted).
* **The Translation:** If they hand you an array and explicitly tell you *"This array is sorted in ascending order,"* 90% of the time, they want you to put a pointer at index `0` and a pointer at the very end, and squeeze them together based on the math.

## 3. The "Heap / Priority Queue" Pattern
* **The Hidden Clues:** "Top K", "Kth largest/smallest", "Most frequent", "K closest".
* **The Translation:** Anytime the problem asks you to keep a "running leaderboard" or find the extreme top/bottom values of a massive dataset, do not sort the whole array! Sorting takes $O(n \log n)$ time. Pushing items into a Heap of size `K` takes $O(n \log k)$ time, which makes the interviewer very happy.

## 4. The "Binary Search" Pattern
* **The Hidden Clues:** "Sorted", "Find a target", OR they give you an explicit constraint: *"You must write an algorithm with $O(\log n)$ runtime complexity."*
* **The Translation:** If an array is sorted, and you need to find something specific, never loop through it one by one. Cut it in half.

## 5. The "Graphs / Grids (DFS & BFS)" Pattern
* **The Hidden Clues:** "2D Grid", "Matrix", "Connected components", "Shortest path", "Minimum steps".
* **The Translation:** * If you see a Grid and need to find "islands" or groupings, use **DFS** (Depth-First Search - exploring all the way down before looking around).
  * If the prompt explicitly asks for the *"Shortest Path"* or *"Minimum Steps"* to reach a target, you **must** use **BFS** (Breadth-First Search - expanding outward layer by layer like a water ripple).

## 6. The "Dynamic Programming" Pattern
* **The Hidden Clues:** "Maximum/Minimum number of ways to...", "Find the optimal strategy", "Choices that affect future choices".
* **The Translation:** If the problem asks you to make decisions (e.g., *"If I rob this house, I can't rob the next one. What is the max money I can make?"*), and doing it by brute force would require checking millions of combinations, it is a DP problem.
