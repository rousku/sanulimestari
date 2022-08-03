# sanulimestari

Profiling (from C:\Users\joonas.harjumaki\git\sanulimestari\prof\combined.prof):                                               
Wed Aug  3 11:28:27 2022    C:\Users\joonas.harjumaki\git\sanulimestari\prof\combined.prof                                     
                                                                                                                               
         34047236 function calls (34046440 primitive calls) in 25.945 seconds                                                  
                                                                                                                               
   Ordered by: cumulative time                                                                                                 
   List reduced from 637 to 20 due to restriction <20>                                                                         
                                                                                                                               
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)                                                        
       14    0.000    0.000   25.944    1.853 runner.py:108(pytest_runtest_protocol)                                           
  278/155    0.001    0.000   25.940    0.167 _hooks.py:244(__call__)                                                          
       14    0.000    0.000   25.939    1.853 runner.py:116(runtestprotocol)                                                   
       42    0.000    0.000   25.939    0.618 runner.py:216(call_and_report)                                                   
  278/155    0.000    0.000   25.939    0.167 _manager.py:77(_hookexec)                                                        
  278/155    0.002    0.000   25.939    0.167 _callers.py:9(_multicall)                                                        
       42    0.000    0.000   25.912    0.617 runner.py:244(call_runtest_hook)                                                 
       42    0.000    0.000   25.911    0.617 runner.py:315(from_call)                                                         
       42    0.000    0.000   25.911    0.617 runner.py:259(<lambda>)                                                          
       14    0.000    0.000   25.896    1.850 runner.py:157(pytest_runtest_call)                                               
       14    0.000    0.000   25.895    1.850 python.py:1759(runtest)                                                          
       14    0.000    0.000   25.895    1.850 python.py:185(pytest_pyfunc_call)                                                
        1    0.000    0.000   25.894   25.894 test_sanulimestari.py:47(test_first_guess)                                       
        1    2.129    2.129   25.894   25.894 __init__.py:93(first_guess)                                                      
 10699441   22.445    0.000   23.395    0.000 __init__.py:79(match)                                                            
22895593/22895571    0.959    0.000    0.959    0.000 {built-in method builtins.len}                                           
        2    0.016    0.008    0.243    0.122 __init__.py:5(parse_words)                                                       
        2    0.000    0.000    0.159    0.080 ElementTree.py:1302(XML)                                                         
        2    0.159    0.080    0.159    0.080 {method 'feed' of 'xml.etree.ElementTree.XMLParser' objects}                     
     3283    0.078    0.000    0.122    0.000 __init__.py:17(guess_word)     