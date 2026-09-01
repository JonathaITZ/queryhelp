[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$pkgs = @(
    'System.Threading.Tasks.Extensions/4.5.4',
    'System.Runtime.CompilerServices.Unsafe/6.0.0',
    'System.Memory/4.5.5',
    'System.Buffers/4.5.1',
    'System.Numerics.Vectors/4.5.0',
    'Google.Protobuf/3.25.1',
    'K4os.Compression.LZ4/1.3.5',
    'K4os.Compression.LZ4.Streams/1.3.5',
    'K4os.Hash.xxHash/1.0.8',
    'BouncyCastle.Cryptography/2.2.1',
    'Microsoft.Bcl.AsyncInterfaces/8.0.0',
    'System.Diagnostics.DiagnosticSource/8.0.0'
)

$destDir = 'C:\Users\dantas.jonatha\.gemini\antigravity\scratch\deps'
if (-not (Test-Path $destDir)) { New-Item -ItemType Directory -Path $destDir -Force | Out-Null }

foreach ($pkg in $pkgs) {
    $parts = $pkg.Split('/')
    $name = $parts[0]
    $ver = $parts[1]
    $destZip = "C:\Users\dantas.jonatha\.gemini\antigravity\scratch\$name.zip"
    $pkgDir = "$destDir\$name"
    if (-not (Test-Path $pkgDir)) {
        Write-Host "Downloading $name $ver..."
        Invoke-WebRequest -Uri "https://www.nuget.org/api/v2/package/$name/$ver" -OutFile $destZip
        Expand-Archive -Path $destZip -DestinationPath $pkgDir -Force
    }
}
Write-Host "Done downloading."
