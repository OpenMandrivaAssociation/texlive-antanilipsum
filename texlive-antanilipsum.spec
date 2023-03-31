Name:		texlive-antanilipsum
Version:	55250
Release:	2
Summary:	Generate sentences in the style of "Amici miei"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/antanilipsum
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/antanilipsum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/antanilipsum.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/antanilipsum.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is an italian blind text generator that ouputs
supercazzole, mocking nonsense phrases from the movie series
Amici Miei ("My friends"), directed by Mario Monicelli.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/antanilipsum
%{_texmfdistdir}/tex/latex/antanilipsum
%doc %{_texmfdistdir}/doc/latex/antanilipsum

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
