# TODO
# - Upstream packages some unfree fonts which we cannot redistribute - use
#   tarball from fc or rip their script.
Summary:	E-book converter and library management
Name:		calibre
Version:	0.6.53
Release:	0.1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://status.calibre-ebook.com/dist/src/%{name}-%{version}.tar.gz
# Source0-md5:	42255d2eb55d1a047d74d3dbb0d0f355
Patch0:		%{name}-prefix.patch
URL:		http://www.calibre-ebook.com/
BuildRequires:	ImageMagick-devel
BuildRequires:	chmlib-devel
BuildRequires:	podofo-devel
BuildRequires:	poppler-Qt-devel
BuildRequires:	python-BeautifulSoup
BuildRequires:	python-PyQt4-devel
BuildRequires:	python-cssutils
BuildRequires:	python-lxml
BuildRequires:	python-mechanize
BuildRequires:	python-sip-devel
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calibre is meant to be a complete e-library solution. It includes
library management, format conversion, news feeds to ebook conversion
as well as e-book reader sync features.

Calibre is primarily a ebook cataloging program. It manages your ebook
collection for you. It is designed around the concept of the logical
book, i.e. a single entry in the database that may correspond to
ebooks in several formats. It also supports conversion to and from a
dozen different ebook formats.

Supported input formats are: MOBI, LIT, PRC, EPUB, CHM, ODT, HTML,
CBR, CBZ, RTF, TXT, PDF and LRS.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_libdir}/%{name}
