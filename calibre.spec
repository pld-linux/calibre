#
# NOTE:
# Upstream packages some unfree fonts which we cannot redistribute,
# so when upgrading calibre we should download upstream tarball by hand from
# http://downloads.sourceforge.net/calibre and run below script in order
# to remove them:
#
# #!/bin/sh
#
# VERSION=$1
#
# rm -rf calibre
# tar -xvzf calibre-$VERSION.tar.gz
# rm -f calibre/resources/fonts/liberation/*
# rm -f calibre/resources/fonts/prs500/*
#
# tar -cvjf calibre-$VERSION-nofonts.tar.bz2 calibre
#
Summary:	E-book converter and library management
Name:		calibre
Version:	0.6.53
Release:	0.1
License:	GPL v3+
Group:		Applications/Multimedia
Source0:	%{name}-%{version}-nofonts.tar.bz2
# Source0-md5:	74f8a83e86820b248eb094bde4f1ab69
Patch0:		%{name}-prefix.patch
URL:		http://www.calibre-ebook.com/
BuildRequires:	ImageMagick-devel
BuildRequires:	chmlib-devel
BuildRequires:	podofo-devel
BuildRequires:	poppler-Qt-devel
BuildRequires:	python-BeautifulSoup
BuildRequires:	python-PIL
BuildRequires:	python-PyQt4-devel
BuildRequires:	python-cssutils
BuildRequires:	python-dateutil
BuildRequires:	python-lxml
BuildRequires:	python-mechanize
BuildRequires:	python-modules-sqlite
BuildRequires:	python-sip-devel
BuildRequires:	rpm-pythonprov
Requires:	python-cssutils
Requires:	python-lxml
Requires:	python-mechanize
Requires:	python-modules-sqlite
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
	--root=$RPM_BUILD_ROOT \
	--libdir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_libdir}/%{name}
