#
# NOTE:
# Upstream packages some unfree fonts which we cannot redistribute,
# so when upgrading calibre we should download upstream tarball by hand from
# http://downloads.sourceforge.net/calibre and run generate-tarball.sh script
# included as SourceX.
#
Summary:	E-book converter and library management
Name:		calibre
Version:	0.6.53
Release:	0.1
License:	GPL v3+
Group:		Applications/Multimedia
Source0:	%{name}-%{version}-nofonts.tar.bz2
# Source0-md5:	7ed89159bbd97db0d2dcf850bb1dd867
Source1:	generate-tarball.sh
Patch0:		%{name}-prefix.patch
Patch1:		%{name}-manpages.patch
Patch2:		%{name}-no-update.patch
Patch3:		%{name}-env_module.patch
Patch4:		%{name}-locales.patch
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
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	sed >= 4.0
BuildRequires:	xdg-utils
Requires:	python-PIL
Requires:	python-cssutils
Requires:	python-dateutil
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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--libdir="%{_libdir}"

# move manpages and locales to proper place
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/man $RPM_BUILD_ROOT%{_mandir}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/localization/locales $RPM_BUILD_ROOT%{_datadir}/locale

# set proper filenames for locales (TODO: switch to patch if possible)
for file in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/messages.mo; do
	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\)/LC_MESSAGES.*:\1:')
	mv $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/messages.mo \
	$RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/%{name}.mo
done;
for file in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/iso639.mo; do
	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\)/LC_MESSAGES.*:\1:')
	mv $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/iso639.mo \
	$RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/%{name}_iso639.mo
done;

# unsupported?
rm -f $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/qt.qm
rm -f $RPM_BUILD_ROOT%{_bindir}/%{name}-uninstall

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYRIGHT README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/*.1*
