#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Pod
%define	pnam	Tree
Summary:	Pod::Tree - Create a static syntax tree for a POD
#Summary(pl):	
Name:		perl-Pod-Tree
Version:	1.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b7558bc5607560b24694d7c2ffdf3d71
BuildRequires:	perl-devel >= 1:5.8
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Stream
BuildRequires:	perl-Pod-Escapes
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C<Pod::Tree> parses a POD into a static syntax tree.  Applications
walk the tree to recover the structure and content of the POD.
See L<C<Pod::Tree::Node>> for a description of the tree.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo ToDo.Not
%{_bindir}/*
%{perl_vendorlib}/Pod/*.pm
%{perl_vendorlib}/Pod/Tree
%{_mandir}/man?/*
