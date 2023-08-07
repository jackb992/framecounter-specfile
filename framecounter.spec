Name:		framecounter
Version:	20171226
Release:	1
Summary:	A small program to count frames in RAW VC-1, MPEG-4 ASP and MPEG-4 AVC streams
License:	custom
BuildRequires:	git
BuildRequires:  qt6-qtbase-devel
Requires:	qt5-qtbase
URL:		https://github.com/Selur/FrameCounter

%description
A small program to count frames in RAW VC-1, MPEG-4 ASP and MPEG-4 AVC streams

%prep
git clone %{url}.git 
cd FrameCounter

%build
cd FrameCounter
qmake FrameCounter.pro;
make

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 FrameCounter/FrameCounter %{buildroot}%{_bindir}/FrameCounter

%files
%{_bindir}/FrameCounter

%changelog
* Mon Aug 07 2023  <> - 20171226
- Initial version
