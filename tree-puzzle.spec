Name:		tree-puzzle
Version:	5.2
Release:	6
Summary:	Maximum likelihood analysis for nucleotide, amino acid and two-state data
Group:		Sciences/Biology
License:	GPL
URL:		http://www.tree-puzzle.de
Source:		http://www.tree-puzzle.de/%{name}-%{version}.tar.bz2

%description
TREE-PUZZLE is a computer program to reconstruct phylogenetic trees 
from molecular sequence data by maximum likelihood. It implements a 
fast tree search algorithm, quartet puzzling, that allows analysis 
of large data sets and automatically assigns estimations of support 
to each internal branch. TREE-PUZZLE also computes pairwise maximum
likelihood distances as well as branch lengths for user specified trees.
In addition, TREE-PUZZLE offers a novel method, likelihood mapping, 
to investigate the support of a hypothesized internal branch without 
computing an overall tree and to visualize the phylogenetic content 
of a sequence alignment. 

%prep
%setup -q

%build
%configure
%make 

%install
%makeinstall_std

%clean

%files
%{_bindir}/*
%doc AUTHORS COPYING ChangeLog README
%doc doc/tree-puzzle.pdf
%doc data/EF.3trees data/globin.a data/globin.trees data/marswolf.n 
%doc data/primates.b data/primates.trees data/EF.phy data/atp6.a 
%doc data/globin.ctrees data/marswolf.ctrees data/marswolf.trees
%doc data/primates.ctrees




