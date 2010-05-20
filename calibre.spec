Summary:	-
Summary(pl.UTF-8):	-
Name:		calibre
Version:	0.6.53
Release:	1
License:	GPL/LGPL/BSD and other
Group:		Applications
Source0:	http://status.calibre-ebook.com/dist/src/%{name}-%{version}.tar.gz
# Source0-md5:	42255d2eb55d1a047d74d3dbb0d0f355
Patch0:		%{name}-prefix.patch
URL:		http://calibre-ebook.com/
BuildRequires:	ImageMagick-devel
BuildRequires:	chmlib-devel
BuildRequires:	podofo-devel
BuildRequires:	poppler-Qt-devel
BuildRequires:	python-PyQt4-devel
BuildRequires:	python-cssutils
BuildRequires:	python-lxml
BuildRequires:	python-mechanize
BuildRequires:	python-sip-devel
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

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
