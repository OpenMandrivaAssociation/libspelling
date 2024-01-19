%define major   1
%define api     1
%define libname %mklibname spelling
%define girname %mklibname spelling-gir %{api}
%define develname %mklibname spelling -d

Name:           libspelling
Version:        0.2.0
Release:        1
Summary:        A spellcheck library for GTK 4
License:        LGPL-2.1-or-later
Group:          System/Libraries/GNOME
URL:            https://gitlab.gnome.org/chergert/libspelling
Source:         https://download.gnome.org/sources/libspelling/0.2/%{name}-%{version}.tar.xz
# Upstream patch to fix license.
Patch0:         https://gitlab.gnome.org/chergert/libspelling/-/commit/7483bd2b80aa0de60ddadbd5348fb70415f5587b.patch

BuildRequires:  meson
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(vapigen)

%description
A spellcheck library for GTK 4.
This library is heavily based upon GNOME Text Editor and GNOME
Builder's spellcheck implementation. However, it is licensed
LGPL-2.1-or-later

%package -n %{libname}
Summary:        Shared libraries for %{name}
Group:          System/Libraries

%description -n %{libname}
Shared libraries for %{name}.

%package -n %{girname}
Summary:        GObject Introspection interface library for %{name}
Group:          System/Libraries

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{develname}
Summary:        Development files for %{name}
Group:          Development/C++
Requires:       %{libname} = %{EVRD}
Requires:       %{girname} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files -n %{libname}
%license COPYING
%doc NEWS README.md
%{_libdir}/libspelling-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Spelling-%{api}.typelib

%files -n %{develname}
%doc %{_datadir}/doc/libspelling-%{api}/
%{_includedir}/libspelling-%{api}/
%{_libdir}/libspelling-%{api}.so
%{_libdir}/pkgconfig/libspelling-%{api}.pc
%{_datadir}/gir-1.0/Spelling-%{api}.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libspelling-%{api}.deps
%{_datadir}/vala/vapi/libspelling-%{api}.vapi
