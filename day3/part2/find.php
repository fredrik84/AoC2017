<?php
  $val = file_get_contents('input');

  $move = 'right';
  $x = 0;
  $y = 0;
  $iter = 0;
  while(true) {
    $sum = 0;
    if($iter != 0) {
      # Check if values are set in a 8 step square around current coordinate
      for($tx = -1; $tx <= 1; $tx++) {
        for($ty = -1; $ty <= 1; $ty++) {
          # If it's set, summarize the values
          if(isset($coords[$x+$tx][$y+$ty])) {
            $sum += $coords[$x+$tx][$y+$ty];
          }
        }
      }
    } else {
      $sum = 1;
    }

    # Save the values so we can iterate them in the next iteration step
    if(!isset($coords[$x][$y]))
      $coords[$x][$y] = $sum;
    # Exit after the value written after input

    if($sum > $val) {
      break;
    }

    # Handle movement in the spiral (could be done better i recon)
    if($move == 'up') {
      if(!isset($coords[$x-1][$y])) {
        $move = 'left';
        $x--;
      } else
        $y++;
    } elseif($move == 'down') {
      if(!isset($coords[$x+1][$y])) {
        $move = 'right';
        $x++;
      } else
        $y--;
    } elseif($move == 'right') {
      if(!isset($coords[$x][$y+1])) {
        $move = 'up';
        $y++;
      } else
        $x++;
    } elseif($move == 'left') {
      if(!isset($coords[$x][$y-1])) {
        $move = 'down';
        $y--;
      } else
        $x--;
    }
    $iter++;
  }
  foreach($coords as $d) {
    foreach($d as $v) {
      $out[] = $v;
    }
  }
  sort($out);
  echo array_pop($out)."\n";
?>
