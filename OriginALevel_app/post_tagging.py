from multiprocessing.resource_sharer import stop
from string import punctuation
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


question_topics = [
    {"code": "1.1.1", "title": "Structure and function of the processor", "content": "Arithmetic, Logic Unit; ALU, Control Unit, Registers (Program Counter; PC, Accumulator; ACC, Memory Address Register; MAR, Memory Data Register; MDR, Current Instruction Register; CIR), bus, busses, data, address and control: how this relates to assembly language programs. The Fetch-Decode-Execute Cycle; including its effects on registers, factors affecting the performance of the CPU: clock speed, number of cores, cache, use of pipelining in a processor to improve efficiency. Von Neumann, Harvard and contemporary processor architecture."},
    {"code": "1.1.2", "title": "Types of processor", "content": "CISC and RISC processors, GPUs and their uses (including those not related to graphics),Multicore and Parallel systems" },
    {"code": "1.1.3", "title": "Input, output and storage", "content": "input, output and storage devices can be applied to the solution of different problems, The uses of magnetic, flash and optical storage devices, RAM and ROM, Virtual storage" },
    {"code": "1.2.1", "title": "Systems Software", "content": "function, operating systems. Memory Management (paging, segmentation and virtual memory).Interrupts, the role of interrupts and Interrupt Service Routines (ISR), role within the Fetch-Decode-Execute Cycle.Scheduling: round robin, first come first served, multi-level feedback queues, shortest job first and shortest remaining time.Distributed, embedded, multi-tasking, multi-user and Real Time operating systems. BIOS Device drivers.Virtual machines, any instance where software is used to take on the function of a machine, including executing intermediate code or running an operating system within another."},
    {"code": "1.2.2", "title": "Applications Generation", "content": "Utilities.Open source vs closed source.Translators: Interpreters, compilers and assemblers.Stages of compilation (lexical analysis, syntax analysis, code generation and optimisation).Linkers and loaders and use of libraries."},
    {"code": "1.2.3", "title": "Software Development", "content": "waterfall lifecycle, agile methodologies, extreme programming, the spiral model and rapid application development.The relative merits and drawbacks of different methodologies and when they might be used.Writing and following algorithms."},
    {"code": "1.2.4", "title": "Types of Programming Language", "content": "characteristics programming paradigms.Procedural languages.Assembly language (including following and writing simple programs with the Little Man Computer instruction set).Modes of addressing memory (immediate, direct,indirect and indexed).Object-oriented languages with an understanding of classes, objects, methods, attributes, inheritance, encapsulation and polymorphism."},
    {"code": "1.3.1", "title": "Compression, Encryption and Hashing", "content": "Lossy vs Lossless compression.Run length encoding and dictionary coding for lossless compression.Symmetric and asymmetric encryption.uses of hashing."},
    {"code": "1.3.2", "title": "Databases", "content": "Relational database, flat file, primary key, foreign key, secondary key, entity relationship modelling, normalisation and indexing.Methods of capturing, selecting, managing and exchanging data.Normalisation to 3NF.SQL Interpret and modifyReferential integrityTransaction processing, ACID (Atomicity, Consistency, Isolation, Durability), record locking and redundancy"},
    {"code": "1.3.3", "title": "Networks", "content": "Characteristics of networks and the importance of protocols and standards.The internet structure: • The TCP/IP Stack. • DNS • Protocol layering. • LANs and WANs. • Packet and circuit switching.Network security and threats, use of firewalls, proxies and encryption.Network hardware Client-server and peer to peer"},
    {"code": "1.3.4", "title": "Web Technologies", "content": "HTML, CSS and JavaScript. Search engine indexing.PageRank algorithm.Server and client side processing."},
    {"code": "1.4.1", "title": "Data Types", "content": "Primitive data types, integer, real/floating point, character, string and Boolean, Represent positive integers in binary.Use of sign and magnitude and two's complement to represent negative numbers in binary. Addition and subtraction of binary integers.Represent positive integers in hexadecimal.Convert positive integers between binary hexadecimal and denary, Representation and normalisation of floating point numbers in binary. Floating point arithmetic, positive and negative numbers, addition and subtraction, Bitwise manipulation and masks: shifts, combining with AND, OR, and XOR.How character sets (ASCII and UNICODE) are used to represent text."},
    {"code": "1.4.2", "title": "Data Structures", "content": "Arrays (of up to 3 dimensions), records, lists, tuples, The following structures to store data: linked-list, graph (directed and undirected), stack, queue, tree, binary search tree, hash table.How to create, traverse, add data to and remove data from the data structures mentioned above. (NB this can be either using arrays and procedural programming or an object-oriented approach)."},
    {"code": "1.4.3", "title": "Boolean Algebra", "content": "Define problems using Boolean logic. Manipulate Boolean expressions, including the use of Karnaugh maps to simplify Boolean expressions.Use the following rules to derive or simplify statements in Boolean algebra: De Morgan's Laws, distribution, association, commutation, double negation.Using logic gate diagrams and truth tables. The logic associated with D type flip flops, half and full adders."},
    {"code": "1.5.1", "title": "Computing related legislation", "content": "The Data Protection Act 1998. The Computer Misuse Act 1990, The Copyright Design and Patents Act 1988. The Regulation of Investigatory Powers Act 2000."},
    {"code": "1.5.2", "title": "Moral and ethical Issues", "content": "moral, social, ethical, cultural, opportunities, risks of digital technology: • Computers in the workforce. • Automated decision making. • Artificial intelligence. • Environmental effects. • Censorship and the Internet. • Monitor behaviour. • Analyse personal information. • Piracy and offensive communications. • Layout, colour paradigms and character sets"},
    {"code": "2.1.1", "title": "Thinking abstractly", "content": "The nature of abstraction. The need for abstraction.The differences between an abstraction and reality, Devise an abstract model for a variety of situations."},
    {"code": "2.1.2", "title": "Thinking ahead", "content": "Identify the inputs and outputs for a given situation.Determine the preconditions for devising a solution to a problem. The nature, benefits and drawbacks of caching.The need for reusable program components."},
    {"code": "2.1.3", "title": "Thinking procedurally", "content": " Identify the components of a problem.Identify the components of a solution to a problem.Determine the order of the steps needed to solve a problem.Identify sub-procedures necessary to solve a problem"},
    {"code": "2.1.4", "title": "Thinking logically", "content": "Identify the points in a solution where a decision has to be taken. Determine the logical conditions that affect the outcome of a decision.Determine how decisions affect flow through a program."},
    {"code": "2.1.5", "title": "Thinking concurrently", "content": "simultaneously, Determine the parts of a problem that can be tackled at the same time.Outline the benefits and trade offs that might result from concurrent processing in a particular situation."},
    {"code": "2.2.1", "title": "Programming techniques", "content": "Programming constructs: sequence, iteration, branching. Recursion, how it can be used and compares to an iterative approach. Global and local variables. Modularity, functions and procedures, parameter passing by value and by reference. Use of an IDE to develop/debug a program.Use of object oriented techniques."},
    {"code": "2.2.2", "title": "Computational methods", "content": "Features that make a problem solvable by computational methods. Problem recognition. Problem decomposition. Use of divide and conquer. Use of abstraction. Learners should apply their knowledge of: • backtracking • data mining • heuristics • performance modelling • pipelining • visualisation to solve problems."},
    {"code": "2.3.1", "title": "Algorithms", "content": "Analysis and design of algorithms for a given situation.The suitability of different algorithms for a given task and data set, in terms of execution time and space. Measures and methods to determine the efficiency of different algorithms, Big O notation (constant, linear, polynomial, exponential and logarithmic complexity). Comparison of the complexity of algorithms. Algorithms for the main data structures, (stacks, queues, trees, linked lists, depth-first (post-order) and breadth-first traversal of trees). Standard algorithms (bubble sort, insertion sort, merge sort, quick sort, Dijkstra’s shortest path algorithm, A* algorithm, binary search and linear search)."},
]




# this functions takes the content as a parameter and it returns the tags
def apply_tag(post_content):
    found_words = []
    auto_tagging = dict() #creating a dictionary with the code and the title from question_topics
    words_in_post = word_tokenize(post_content) 
    tokens_without_sw = [word for word in words_in_post if not word in stopwords.words() and not word in punctuation]
    tokens_without_sw.extend(['I', "n't", "you", "me",])

    for word in tokens_without_sw:
        for item in question_topics:
            #  the words in the distionaries can be recognised if typed in lower case or upper case. 
            if word.lower() in word_tokenize(item['content'].lower()):
                # checks if the user has enetered 3 or more keywords. If they had then the question will get categorised
                found_words.append(word)
                if len(found_words) >= 3:
                    auto_tagging = {'code':item['code'], 'title':item['title']}
    return auto_tagging, found_words


