# sanulimestari

Profiling (from C:\Users\joonas.harjumaki\git\sanulimestari\prof\combined.prof):                                               
Wed Aug  3 17:14:10 2022    C:\Users\joonas.harjumaki\git\sanulimestari\prof\combined.prof                                     
                                                                                                                               
         2061914008 function calls (1714747372 primitive calls) in 5607.441 seconds                                            
                                                                                                                               
   Ordered by: cumulative time                                                                                                 
   List reduced from 640 to 20 due to restriction <20>                                                                         
                                                                                                                               
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)                                                        
       14    0.000    0.000 5607.440  400.531 runner.py:108(pytest_runtest_protocol)                                           
  278/155    0.001    0.000 5607.436   36.177 _hooks.py:244(__call__)                                                          
       14    0.000    0.000 5607.435  400.531 runner.py:116(runtestprotocol)                                                   
       42    0.000    0.000 5607.435  133.510 runner.py:216(call_and_report)                                                   
  278/155    0.000    0.000 5607.435   36.177 _manager.py:77(_hookexec)                                                        
  278/155    0.002    0.000 5607.435   36.177 _callers.py:9(_multicall)                                                        
       42    0.000    0.000 5607.404  133.510 runner.py:244(call_runtest_hook)                                                 
       42    0.000    0.000 5607.403  133.510 runner.py:315(from_call)                                                         
       42    0.000    0.000 5607.403  133.510 runner.py:259(<lambda>)                                                          
       14    0.000    0.000 5607.387  400.528 runner.py:157(pytest_runtest_call)                                               
       14    0.000    0.000 5607.387  400.528 python.py:1759(runtest)                                                          
       14    0.000    0.000 5607.387  400.528 python.py:185(pytest_pyfunc_call)                                                
        1    0.000    0.000 5607.386 5607.386 test_sanulimestari.py:47(test_first_guess)                                       
        1  110.505  110.505 5607.385 5607.385 __init__.py:105(first_guess)                                                     
   290477  164.876    0.001 4976.593    0.017 __init__.py:94(get_word_count)                                                   
950150267 4639.083    0.000 4811.717    0.000 __init__.py:80(match)                                                            
 10699453  231.957    0.000  363.763    0.000 __init__.py:18(guess_word)                                                       
-228949637/-228949659  189.343   -0.000  189.343   -0.000 {built-in method builtins.len}                                       
60294561/10699441   59.428    0.000  156.277    0.000 __init__.py:118(tuple2list)                                              
357865281/60294561   74.456    0.000  144.225    0.000 __init__.py:119(<genexpr>)      