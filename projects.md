---
layout: page
title: Projects
---

## Echoes of the Subterra Game
A Shoot em Up game developed over the course of 2 months for a game development class. Written in the Wolfie2D engine,
it involved writing custom engine and rendering code and roughly 30,000 lines of additional code total. All the 
assets and are custom made for this game.

<a href=https://echo-of-the-subterra.web.app/> Play it here.</a>
<img src="/assets/EOSTtitle.png"/>
<img src="/assets/EOSTgameplay.png"/>

## Decaf Compiler
Developed a compiler that takes a program written in Decaf, a language modeled after Java, and compiles it 
to abstract machine code. Written in Python over the course of a semester.
Ex.

<pre><code>class test029
{
    public static void main()
    {   
        int a;
        a = 0;
        while (a < 10)
        {
            a = a + 1;
        }
    }
}</code></pre>
Gets compiled to...
<pre><code>.static_data 0
M_main_4:
    move_immed_i t1, 0
    move t0, t1 #assign
L0: #while loop condition
    move_immed_i t3, 10
    lt t2, t0, t3 #lt
    bz t2, L1 #loop cond branch
    move_immed_i t5, 1
    iadd t4, t0, t5 #add
    move t0, t4 #assign
    jmp L0
L1: #end while</code></pre>

## Hitbox
Platforming game I worked on in my free time.
<video width="640" preload="auto" muted controls>
  <source src="/assets/hitbox.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

## Mancala in Python
An implementation of the board game Mancala in python. Also includes several mancala playing bots with different strategies. 
Compared the winloss ratio of every bot in a chart.
<img src="/assets/mancala.png"/>

Try playing against the best bot by downloading the <a href="/assets/mancala.py">Mancala python script</a>.

##Fake Stack Overflow
A webapp made in a software development class using the MERN (Mongoose, Express, React, Node.js) stack to deliver similar
functionality to stack overflow. Users could post questions, and other users could vote on those questions and answer them.

##Sheets2App
A webapp meant to mimic Google AppSheets, where users can create apps without writing any code 
that interact with google sheets as a backend.
<img src="/assets/S2A.png"/>

