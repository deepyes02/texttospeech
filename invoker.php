<?php

$command = escapeshellcmd("/Users/deepeshdhakal/Desktop/text-to-speech/text-to-speech.py 'जिन्दगी छोटो छ' 'ne'");
$output = shell_exec($command);
echo $output;