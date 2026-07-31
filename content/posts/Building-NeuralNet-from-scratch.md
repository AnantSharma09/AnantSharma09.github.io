---
title: "Understanding Neural Networks from Scratch (Part 1)"
date: "2026-07-30"
summary: "My journey of implementing the same neural network in two different ways: first using a scalar computational graph with automatic differentiation, and then using fully vectorized NumPy with manually derived backpropagation."
tags:
  - Deep Learning
  - Autograd
  - Backpropagation
  - Micrograd
  - Numpy
---

### **Interviewr:** What is a Neural Networks?

### **Me:** It's a network of neurons that learns predicts the output for a given problem.

### **Inverviewr:** But *why* does a neural network work? Why is a simple linear function, `Wx + b`, not enough? Why does adding an activation function suddenly make it capable of learning? And why does stacking these layers together allow it to solve incredibly complex problems?


### **Me:** ......                                           Sorry, I don't know!!!

Most people in machine learning can answer **what** a neural network is. Far fewer can confidently explain **why** it works.That realization bothered me.

I didn't want to be someone who could build models with PyTorch but couldn't explain what was actually happening underneath. I wanted to understand why backpropagation works, why gradients point in the right direction, why activation functions are necessary, and how thousands or even billions of parameters somehow learn meaningful representations from data.

This blog series is my attempt to answer those questions from first principles.Rather than treating neural networks as a black box, I'll build them from scratch in two different ways.

- **Implementation 1:** A scalar computational graph with automatic differentiation, inspired by Micrograd.
- **Implementation 2:** A fully vectorized NumPy implementation with manually derived matrix backpropagation.

Only after understanding both approaches will I move on to PyTorch, where the abstractions actually make sense instead of feeling like magic.The goal isn't just to build another neural network. It's to understand *why* every line of code exists.

