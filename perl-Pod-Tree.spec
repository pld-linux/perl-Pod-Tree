#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Pod
%define	pnam	Tree
Summary:	Pod::Tree - create a static syntax tree for a POD
Summary(pl):	Pod::Tree - tworzenie statycznych drzew sk³adniowych dla POD
Name:		perl-Pod-Tree
Version:	1.10
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b7558bc5607560b24694d7c2ffdf3d71
Patch0:		%{name}-carriage_return.patch
Patch1:		%{name}-item_warning.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Stream
BuildRequires:	perl-Pod-Escapes
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod::Tree parses a POD into a static syntax tree. Applications walk
the tree to recover the structure and content of the POD. See
Pod::Tree::Node manual for a description of the tree.

%description -l pl
Pod::Tree przekszta³ca POD na statyczne drzewo sk³adniowe. Aplikacje
wêdruj± po drzewie w celu uzyskania struktury i zawarto¶ci z POD. Opis
drzewa mo¿na znale¼æ w manualu do Pod::Tree::Node.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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

# confilcts with pod2html from perl-tools-pod
rm -f $RPM_BUILD_ROOT%{_bindir}/pod2html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo ToDo.Not
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Pod/*.pm
%{perl_vendorlib}/Pod/Tree
%{_mandir}/man?/*
%{_examplesdir}/%{name}-%{version}
