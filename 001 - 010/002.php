<?php

  $term0 = 1;
  $term1 = 2;
  $termsum = 0;

  while($term1 < 4000000) {
    if ($term1 % 2 == 0) {
      $termsum += $term1;
    }
    $term1 += $term0;
    $term0 = $term1 - $term0;
  }

  print($termsum);
