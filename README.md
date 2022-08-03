# sanulimestari

Profiling (from C:\Users\joonas.harjumaki\git\sanulimestari\prof\combined.prof):                                               
Wed Aug  3 11:26:47 2022    C:\Users\joonas.harjumaki\git\sanulimestari\prof\combined.prof                                     
                                                                                                                               
         147579341 function calls (147578545 primitive calls) in 52.071 seconds                                                
                                                                                                                               
   Ordered by: cumulative time                                                                                                 
   List reduced from 637 to 20 due to restriction <20>                                                                         
                                                                                                                               
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)                                                        
       14    0.000    0.000   52.070    3.719 runner.py:108(pytest_runtest_protocol)                                           
       14    0.000    0.000   52.066    3.719 runner.py:116(runtestprotocol)                                                   
  278/155    0.001    0.000   52.066    0.336 _hooks.py:244(__call__)                                                          
       42    0.000    0.000   52.065    1.240 runner.py:216(call_and_report)                                                   
  278/155    0.000    0.000   52.065    0.336 _manager.py:77(_hookexec)                                                        
  278/155    0.002    0.000   52.065    0.336 _callers.py:9(_multicall)                                                        
       42    0.000    0.000   52.035    1.239 runner.py:244(call_runtest_hook)                                                 
       42    0.000    0.000   52.035    1.239 runner.py:315(from_call)                                                         
       42    0.000    0.000   52.034    1.239 runner.py:259(<lambda>)                                                          
       14    0.000    0.000   52.019    3.716 runner.py:157(pytest_runtest_call)                                               
       14    0.000    0.000   52.018    3.716 python.py:1759(runtest)                                                          
       14    0.000    0.000   52.018    3.716 python.py:185(pytest_pyfunc_call)                                                
        1    0.000    0.000   52.017   52.017 test_sanulimestari.py:47(test_first_guess)                                       
        1    2.310    2.310   52.017   52.017 __init__.py:93(first_guess)                                                      
 10699441   34.429    0.000   49.314    0.000 __init__.py:79(match)                                                            
113533286   13.785    0.000   13.785    0.000 {method 'startswith' of 'str' objects}                                           
22895593/22895571    1.109    0.000    1.109    0.000 {built-in method builtins.len}                                           
        2    0.017    0.009    0.239    0.119 __init__.py:5(parse_words)                                                       
        2    0.000    0.000    0.166    0.083 ElementTree.py:1302(XML)                                                         
        2    0.166    0.083    0.166    0.083 {method 'feed' of 'xml.etree.ElementTree.XMLParser' objects}
