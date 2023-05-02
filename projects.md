---
layout: page
title: Projects
---

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

## Ableton User Instructions
User instructions for <a href="https://docs.google.com/document/d/1ccjKEBXLTS8tJAEKt3Mbrwhw_P5l8udo1hT_qEmavPY/edit?usp=sharing">how to use sidechain compression in Ableton Live</a>.

## Research Press Release
<a href="https://docs.google.com/document/d/1QCzwFYvMMrfm0l6h5qRWxCgzOP8OHKOE0mBQsCE7dW8/edit?usp=sharing">A press release</a> detailing new research developments by Stony Brook University about the population collapse of scallops near Long Island.