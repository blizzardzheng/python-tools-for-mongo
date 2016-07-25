# !/bin/bash
short=(r1tBtUcV BkAgcU54 rk7zqLq4 S10ItdcN SkMKtd54 S11sEF9V rkLp4KcV HycxSF5E SkufBF5E BJA4BYcN HkHPrt54 H14FSY9N
SympqUqN SyVRc85N Hkwyi8cE SJ-SiLq4 ByAro8cV H1nLiL94 HyivsI9N By4Ys85E SyEss8cN rJRvOdqE rJHKdu9E B1rcdO9N S1zsducE
Skx2u_cE HyRhdd54 rJa6_ucN HJx1F_c4 ryh1KdqV)

echo ${#short[*]}

for ((i=0; i<${#short[*]}; i++))
do
  python url_shortlener_detect.py ${short[$i]} $1
  echo ${i}
done
