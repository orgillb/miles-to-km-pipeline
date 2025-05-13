[Setup]
AppName=Miles to Kilometers Converter
AppVersion=1.0
DefaultDirName={pf}\MilesToKm
DefaultGroupName=Miles to Kilometers Converter
OutputDir=.
OutputBaseFilename=MilesToKmInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Users\Brett\Documents\deployment and automated test engineer\dist\miles_to_km.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Miles to KM Converter"; Filename: "{app}\miles_to_km.exe"
