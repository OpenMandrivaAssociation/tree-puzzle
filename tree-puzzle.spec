%define name	tree-puzzle
%define version 5.2
%define rel	6
%define release %mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Maximum likelihood analysis for nucleotide, amino acid and two-state data
Group:		Sciences/Biology
License:	GPL
URL:		http://www.tree-puzzle.de
Source:		http://www.tree-puzzle.de/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%doc AUTHORS COPYING ChangeLog README
%doc doc/tree-puzzle.pdf
%doc data/EF.3trees data/globin.a data/globin.trees data/marswolf.n 
%doc data/primates.b data/primates.trees data/EF.phy data/atp6.a 
%doc data/globin.ctrees data/marswolf.ctrees data/marswolf.trees
%doc data/primates.ctrees




%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 5.2-6mdv2011.0
+ Revision: 615238
- the mass rebuild of 2010.1 packages

* Mon Mar 15 2010 Eric Fernandez <zeb@mandriva.org> 5.2-5mdv2010.1
+ Revision: 519809
- bump release version and rebuild

* Wed May 06 2009 Eric Fernandez <zeb@mandriva.org> 5.2-4mdv2010.0
+ Revision: 372573
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 5.2-3mdv2009.0
+ Revision: 140921
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 19 2006 Eric Fernandez <zeb@mandriva.org> 5.2-3mdv2007.0
+ Revision: 100252
- Import tree-puzzle

* Mon Jun 26 2006 Eric Fernandez <zeb@zebulon.org.uk> 5.2-3mdv2007.0
- rebuild
- use mkrel

* Wed Nov 02 2005 Guillaume Rousse <guillomovitch@mandriva.org> 5.2-2mdk
- %%mkrel 
- spec cleanup

* Sat Oct 02 2004 Guillaume Rousse <guillomovitch@mandrake.org> 5.2-1mdk 
- first mdk release with a spec stolen from Luc Ducazu <luc@biolinux.org>

