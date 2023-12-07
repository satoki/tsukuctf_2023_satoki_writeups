# EXECpy

## 問題文
RCEがめんどくさい？  
データをexecに渡しといたからRCE2XSSしてね！  

<URL>TODO  

[EXECpy.zip](files/EXECpy.zip)  

## 難易度
**easy**  

## 作問にあたって
DEF CON 31で小さく開催されていたSpaceX Security Challengeにpotetisenseiと出た際のテクニックをXSSに落とし込みました。  
pickleでRCEができるシナリオでサーバ内部のバイナリを取得する必要があったのですが、アウトバウンド通信や応答時間でのオラクルができない(共に運営インフラの問題)状況でした。  
そこで開いているfdに取得したいデータを流し込んでHTTP応答として返すことで、入手する手法を用いていました。  
現実ではXSS2RCEは最高ですが、RCE2XSSはうれしくないです。  

## 解法
TODO  

## TsukuCTF23{175_4_73rr1bl3_4774ck_70_1n73rrup7_h77p}
