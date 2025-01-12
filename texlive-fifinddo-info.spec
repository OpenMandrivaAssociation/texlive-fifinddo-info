Name:		texlive-fifinddo-info
Version:	29349
Release:	2
Summary:	German HTML beamer presentation on nicetext and morehype
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/fifinddo-info
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fifinddo-info.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fifinddo-info.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fifinddo-info.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The bundle: - exhibits the process of making an "HTML beamer
presentation" with the blogdot package from the morehype
bundle, and - offers a sketch (in German) of package
documentation and HTML generation based on the fifinddo
package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/fifinddo-info/LIESMICH.txt
%doc %{_texmfdistdir}/doc/latex/fifinddo-info/README
%doc %{_texmfdistdir}/doc/latex/fifinddo-info/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/latex/fifinddo-info/dante-mv45-lueck.pdf
%doc %{_texmfdistdir}/doc/latex/fifinddo-info/dantev45.htm
%doc %{_texmfdistdir}/doc/latex/fifinddo-info/mdoccorr.pdf
%doc %{_texmfdistdir}/doc/latex/fifinddo-info/variants/dantev45-1180-clean.html
%doc %{_texmfdistdir}/doc/latex/fifinddo-info/variants/dantev45-1180-com.html
%doc %{_texmfdistdir}/doc/latex/fifinddo-info/variants/dantev45-768-com.html
%doc %{_texmfdistdir}/doc/latex/fifinddo-info/variants/dantev45-768-exact-frame.html
%doc %{_texmfdistdir}/doc/latex/fifinddo-info/variants/dantev45-768-exact-show.html
%doc %{_texmfdistdir}/doc/latex/fifinddo-info/variants/dantev45-768-filltype-show.html
%doc %{_texmfdistdir}/doc/latex/fifinddo-info/variants/dantev45-992-com.html
%doc %{_texmfdistdir}/doc/latex/fifinddo-info/variants/dantev45-992-exact-frame.html
%doc %{_texmfdistdir}/doc/latex/fifinddo-info/variants/dantev45-992-exact.html
#- source
%doc %{_texmfdistdir}/source/latex/fifinddo-info/SrcFILEs.txt
%doc %{_texmfdistdir}/source/latex/fifinddo-info/makeelse/expose.tex
%doc %{_texmfdistdir}/source/latex/fifinddo-info/makeelse/mdoccorr.tex
%doc %{_texmfdistdir}/source/latex/fifinddo-info/makeelse/srcfiles.tex
%doc %{_texmfdistdir}/source/latex/fifinddo-info/makeelse/updsfl.sh
%doc %{_texmfdistdir}/source/latex/fifinddo-info/makeone/dantev45.fdf
%doc %{_texmfdistdir}/source/latex/fifinddo-info/makeone/dantev45.tex
%doc %{_texmfdistdir}/source/latex/fifinddo-info/makeone/makedot.tex
%doc %{_texmfdistdir}/source/latex/fifinddo-info/makevars/bashvars.sh
%doc %{_texmfdistdir}/source/latex/fifinddo-info/makevars/dantev45.cfg
%doc %{_texmfdistdir}/source/latex/fifinddo-info/makevars/longdan.sh
%doc %{_texmfdistdir}/source/latex/fifinddo-info/makevars/makedots.tex
%doc %{_texmfdistdir}/source/latex/fifinddo-info/makevars/texvars.sh

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc source %{buildroot}%{_texmfdistdir}
