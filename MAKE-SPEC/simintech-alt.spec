%define DISTR_NAME alt
Name:		simintech
Version:	1.0.0.0
Release:	0.%{?DISTR_NAME}
Summary:	SimInTech (Simulation In Technic) is an environment for the development of mathematical models, control algorithms, control interfaces and automatic code generation for control controllers and graphic displays.
Summary(ru):	SimInTech (Simulation In Technic) – среда разработки математических моделей, алгоритмов управления, интерфейсов управления и автоматической генерации кода для контроллеров управления и графических дисплеев.

Group:		Sciences/Other
License:	3VServices
URL:		http://simintech.ru/index.html
Source0:	config.tar.gz
Source1:	simintech.desktop
#patch0:		update-package-export-to-support-DESTDIR.diff
#patch1:		update-paths-for-FHS.diff
#собираем проект, внутри свои либы... А при установке эти либы не нужно искать на стандартных местах.
AutoReqProv:    no
Autoprov: 0

##  Зависимости
BuildRequires:  glibc 


Requires:	libGLU
Requires:	shared-desktop-icons

#собираем проект, внутри свои либы... А при установке эти либы не нужно искать на стандартных местах.
#Отключаем это:
%define __find_requires /bin/true
#По аналогии отключаем авто provides:
%define __find_provides /bin/true

%description
SimInTech (Simulation In Technic) is an environment for the development of mathematical models, control algorithms, control interfaces and automatic code generation for control controllers and graphic displays.
SimInTech is designed for detailed research and analysis of non-stationary processes in various control objects.

%description -l ru
SimInTech (Simulation In Technic) – среда разработки математических моделей, алгоритмов управления, интерфейсов управления и автоматической генерации кода для контроллеров управления и графических дисплеев.
SimInTech предназначен для детального исследования и анализа нестационарных процессов в различных объектах управления. 

%global debug_package %{nil}

%prep
%setup -n %{_builddir}/config

%build
%configure

%install
mkdir -p %{buildroot}/opt
mkdir -p %{buildroot}/opt/simintech
#tar -xvzf %{_sourcedir}/simintech.tar.gz -C %{buildroot}/opt
tar -xvzf %{_sourcedir}/simintech_rus_linux.tgz -C %{buildroot}/opt/simintech
#Необходимо удалять файлы *.lib, иначе вываливается ошибка
#file in wrong format ошибка: Неверный код возврата из /var/tmp/rpm-tmp.ZuKXzp 
find %{buildroot}/opt/simintech/ -type f -name "*.lib" -delete


#Icon
mkdir -p %{buildroot}/usr
mkdir -p %{buildroot}/usr/share/
mkdir -p %{buildroot}/usr/share/applications/
cp -f %{_sourcedir}/simintech.desktop %{buildroot}/usr/share/applications/

#mkdir -p %{buildroot}/usr/share/Desktop/
#cp -f %{_sourcedir}/simintech.desktop %{buildroot}/usr/share/Desktop/

mkdir -p %{buildroot}/usr/share/icons/
mkdir -p %{buildroot}/usr/share/icons/hicolor/
mkdir -p %{buildroot}/usr/share/icons/hicolor/48x48/
mkdir -p %{buildroot}/usr/share/icons/hicolor/48x48/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/64x64/
mkdir -p %{buildroot}/usr/share/icons/hicolor/64x64/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/128x128/
mkdir -p %{buildroot}/usr/share/icons/hicolor/128x128/apps
cp -f %{_sourcedir}/48x48/simintech.png %{buildroot}/usr/share/icons/hicolor/48x48/apps
cp -f %{_sourcedir}/64x64/simintech.png %{buildroot}/usr/share/icons/hicolor/64x64/apps
cp -f %{_sourcedir}/128x128/simintech.png %{buildroot}/usr/share/icons/hicolor/128x128/apps


%files
/opt/simintech/*
/usr/share/applications/simintech.desktop
#/usr/share/Desktop/simintech.desktop
/usr/share/icons/hicolor/48x48/apps/simintech.png
/usr/share/icons/hicolor/64x64/apps/simintech.png
/usr/share/icons/hicolor/128x128/apps/simintech.png

%postun 
rm -rf /opt/simintech/ 
rm -f /usr/share/applications/simintech.desktop
#rm -f /usr/share/Desktop/simintech.desktop

%changelog

