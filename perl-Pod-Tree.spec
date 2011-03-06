#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Pod
%define		pnam	Tree
Summary:	Pod::Tree - create a static syntax tree for a POD
Summary(pl.UTF-8):	Pod::Tree - tworzenie statycznych drzew składniowych dla POD
Name:		perl-Pod-Tree
Version:	1.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Pod/SWMCD/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7ab2dc16736ce37d1bf82e6065107cf5
Patch0:		%{name}-carriage_return.patch
Patch1:		%{name}-item_warning.patch
URL:		http://search.cpan.org/dist/Pod-Tree/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Stream
BuildRequires:	perl-IO >= 1.23
BuildRequires:	perl-Pod-Escapes
BuildRequires:	perl-Text-Template
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod::Tree parses a POD into a static syntax tree. Applications walk
the tree to recover the structure and content of the POD. See
Pod::Tree::Node manual for a description of the tree.

%description -l pl.UTF-8
Pod::Tree przekształca POD na statyczne drzewo składniowe. Aplikacje
wędrują po drzewie w celu uzyskania struktury i zawartości z POD. Opis
drzewa można znaleźć w manualu do Pod::Tree::Node.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a skeleton $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo ToDo.Not
%attr(755,root,root) %{_bindir}/mod2html
%attr(755,root,root) %{_bindir}/perl2html
%attr(755,root,root) %{_bindir}/pods2html
%attr(755,root,root) %{_bindir}/podtree2html
%{perl_vendorlib}/Pod/Tree.pm
%{perl_vendorlib}/Pod/Tree
%{_mandir}/man1/mod2html.1p*
%{_mandir}/man1/perl2html.1p*
%{_mandir}/man1/pods2html.1p*
%{_mandir}/man1/podtree2html.1p*
%{_mandir}/man3/Pod::Tree*.3pm*
%{_examplesdir}/%{name}-%{version}
