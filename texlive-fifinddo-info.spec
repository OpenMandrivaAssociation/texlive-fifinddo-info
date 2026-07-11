%global tl_name fifinddo-info
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1b
Release:	%{tl_revision}.1
Summary:	German HTML beamer presentation on nicetext and morehype
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/fifinddo-info
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fifinddo-info.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fifinddo-info.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fifinddo-info.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle: exhibits the process of making an "HTML beamer presentation"
with the blogdot package from the morehype bundle, and HTML generation
based on the fifinddo package.

