<?php

$command = escapeshellcmd('/Users/deepeshdhakal/Desktop/text-to-speech/text-to-speech.py');
$output = shell_exec($command);
echo $output;