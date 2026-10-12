# Most interviewers won't ask you to memorize BFS/DFS. Instead, they'll ask problems like:
# Number of Islands ⭐⭐⭐⭐⭐
# Flood Fill
# Clone Graph
# Course Schedule
# Binary Tree Level Order Traversal
# Maximum Depth of Binary Tree
# Connected Components

# Here's a list of the most frequently asked Python interview questions.

# 1. Python Internals
# What is Python?
# Why is Python dynamically typed?
# What is duck typing?
# How is Python interpreted?
# What is bytecode?
# What is the Global Interpreter Lock (GIL)?
# Why does Python have a GIL?
# How does Python manage memory?
# What is reference counting?
# What is garbage collection?
# Difference between stack and heap memory.
# 2. OOP
# What are the four pillars of OOP?
# Difference between abstraction and encapsulation.
# Method overriding vs overloading.
# What is multiple inheritance?
# What is MRO?
# Explain C3 Linearization.
# What is super()?
# Class method vs static method vs instance method.
# What are abstract classes?
# What are metaclasses?
# 3. Functions
# What are first-class functions?
# What are higher-order functions?
# What are closures?
# What are decorators?
# Write a decorator with arguments.
# Explain *args and **kwargs.
# Lambda functions.
# Generator functions.
# Iterator vs Iterable.
# yield vs return.
# 4. Data Structures
# List vs Tuple.
# Set vs Dictionary.
# When would you use a tuple?
# Dictionary internals.
# Why are dictionaries O(1)?
# What is hashing?
# Mutable vs immutable.
# Deep copy vs shallow copy.
# Explain copy.deepcopy().
# 5. String Questions
# Reverse a string.
# Check palindrome.
# Find duplicate characters.
# Count frequency.
# Most common character.
# Anagram check.
# 6. List Questions
# Remove duplicates.
# Flatten nested lists.
# Merge sorted lists.
# Find second largest.
# Rotate a list.
# Move zeros to the end.
# Find missing number.
# 7. Coding Problems
# Two Sum.
# FizzBuzz.
# Valid Parentheses.
# Longest Substring Without Repeating Characters.
# Merge Intervals.
# Binary Search.
# BFS and DFS.
# LRU Cache.
# Top K Frequent Elements.
# Sliding Window Maximum.
# 8. Exception Handling
# try, except, finally.
# Custom exceptions.
# Raise vs assert.
# Exception hierarchy.
# 9. File Handling
# Read/write files.
# CSV handling.
# JSON handling.
# Context manager (with).
# Why use with?
# 10. Multithreading & Multiprocessing
# Thread vs Process.
# Multithreading vs Multiprocessing.
# GIL.
# ThreadPoolExecutor.
# ProcessPoolExecutor.
# Async vs Threads.
# Race condition.
# Deadlock.
# 11. Async Python
# What is asyncio?
# Event loop.
# async and await.
# Coroutine.
# When to use async.
# Async vs multiprocessing.
# 12. Memory Optimization
# What is __slots__?
# Generators vs Lists.
# Lazy loading.
# Memory profiling.
# Weak references.
# 13. Python Internals
# __dict__
# __new__
# __init__
# __str__
# __repr__
# __call__
# __len__
# __iter__
# __next__
# __enter__
# __exit__
# 14. Decorators
# Authentication decorator.
# Timing decorator.
# Logging decorator.
# Retry decorator.
# Caching decorator.
# 15. Generators
# Infinite generator.
# Fibonacci generator.
# Why generators are memory efficient.
# 16. Context Managers
# How does with work?
# Create your own context manager.
# contextlib.
# 17. Database (Python)
# Connect to PostgreSQL.
# Connection pooling.
# SQL Injection prevention.
# ORM vs Raw SQL.
# Transactions.
# Bulk insert.
# 18. Django/FastAPI
# Django request lifecycle.
# Middleware.
# Signals.
# Authentication.
# Sessions.
# JWT.
# ORM optimization.
# select_related() vs prefetch_related().
# Caching.
# Celery.
# 19. REST APIs
# PUT vs PATCH.
# Idempotency.
# Pagination.
# Rate limiting.
# Versioning.
# Authentication.
# OAuth.
# JWT.
# API Gateway.
# 20. AWS (Common for Backend)
# EC2.
# S3.
# IAM.
# Lambda.
# API Gateway.
# SQS.
# SNS.
# ECS.
# EKS.
# Fargate.
# CloudWatch.
# VPC.
# 21. Docker
# Dockerfile.
# Image vs Container.
# Volumes.
# Networks.
# Multi-stage builds.
# ENTRYPOINT vs CMD.
# 22. Linux
# grep
# awk
# sed
# ps
# top
# netstat
# lsof
# find
# chmod
# chown
# 23. Design Patterns
# Singleton.
# Factory.
# Strategy.
# Observer.
# Builder.
# Adapter.
# Decorator Pattern.
# 24. System Design
# URL Shortener.
# Notification Service.
# Chat Application.
# File Upload Service.
# Payment Gateway.
# Inventory Management.
# Rate Limiter.
# 25. Performance
# Profile Python code.
# Optimize SQL queries.
# N+1 query problem.
# Caching.
# Redis.
# Load balancing.
# 26. Testing
# pytest
# Mocking.
# Fixtures.
# Unit vs Integration tests.
# Coverage.
# 27. Frequently Asked "Why?" Questions
# Why is Python slow?
# Why use generators?
# Why use tuples?
# Why use Redis?
# Why use Docker?
# Why use Celery?
# Why use Kafka instead of RabbitMQ?
# Why use PostgreSQL over MySQL?
# Why use FastAPI instead of Flask?
# Why use asyncio?
# 🎯 Top 30 "Must Know" Questions

# If you have limited time, master these first:

# Decorators
# Closures
# *args and **kwargs
# MRO
# super()
# GIL
# Multithreading vs Multiprocessing
# Async/Await
# Generators
# Iterators
# Context Managers
# __new__ vs __init__
# __slots__
# Shallow Copy vs Deep Copy
# Mutable vs Immutable
# List vs Tuple
# Dictionary Internals
# Hashing
# Garbage Collection
# Reference Counting
# SQL Injection Prevention
# REST API Design
# JWT Authentication
# Docker Basics
# Redis Caching
# Celery
# Factory Pattern
# Singleton Pattern
# LRU Cache
# Binary Search


# To use: pip install memory_profiler
from memory_profiler import profile

@profile
def memory_intensive_task():
    a = [1] * (10**6)  # Spikes memory
    b = [2] * (2 * 10**7)
    del b
    return a
memory_intensive_task()
# Running this outputs a line-by-line breakdown of RAM consumption.

