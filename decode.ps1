function Decode-HeidiPassword($hex) {
    if (-not $hex -or $hex.Length -lt 2) { return "" }
    $shift = [int]::Parse($hex[$hex.Length - 1].ToString())
    $cleanHex = $hex.Substring(0, $hex.Length - 1)
    $res = ""
    for ($i = 0; $i -lt $cleanHex.Length; $i += 2) {
        $byte = [Convert]::ToInt32($cleanHex.Substring($i, 2), 16)
        $res += [char]($byte - $shift)
    }
    return $res
}

Write-Host "AWS:" (Decode-HeidiPassword "7B793E723F6C4C5F3D3B78758")
Write-Host "AWS2:" (Decode-HeidiPassword "7674396D3A67475A383673703")
Write-Host "GLACAI:" (Decode-HeidiPassword "498137593F3E3768665653383E7854557")
Write-Host "Softcomshop:" (Decode-HeidiPassword "77536F6C75803F3E6")
