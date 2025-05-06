# FASTA Sequence Analysis and GC Content Visualization

## Project Overview

This project processes DNA sequences from a FASTA file, performs essential analyses such as GC content calculation, sequence length measurement, and k-mer frequency counting. The results are exported to CSV and visualized using matplotlib.

## Motivation

Analyzing GC content and k-mer patterns is a fundamental step in bioinformatics. These features help in understanding gene composition, identifying species-specific motifs, and providing potential data for machine learning.

## Dataset and Visualizations

Input: 
FASTA file

CSV Output:
Sequence ID
Sequence Length
GC Content (%)
First 50 bases (preview)

k-mer Output:
Table of k-mer frequencies (default k=3)

Visualizations:
Histogram of GC content distribution

## Project Worksteps

-Load FASTA sequences using Biopython
-Compute length, GC content, k-mer frequency for each sequence
-Export summary table to CSV
-Visualize with matplotlib

## Screenshots

![分析結果](images/截圖%202025-05-06%20下午11.25.03.png)
![分析結果](images/截圖%202025-05-06%20下午11.25.12.png)

## How to use?

Run each cell step by step with Jupyter notebook to understand the process.

