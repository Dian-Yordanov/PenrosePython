__author__ = 'zyan'

import sys
sys.path.append('/home/zyan/jython2.7rc1/jython.jar')
import org.python.core.*;
import java.util.*;

public class TestDict
{
 public Hashtable data;

 public TestDict()
 {
  data = new Hashtable();
 }
 public void __setitem__(String key, String value)
 {
  data.put(key, value);
  System.out.println("Added key \"" + key + "\" value: \"" +
         value + "\"");
 }
 public String __getitem__(String key)
 {
  if (data.containsKey(key))
  {
   String value = (String)data.get(key);
   System.out.println("Found key \"" + key + "\" value: \"" +
         value + "\"");
   return value;
  }
  else
  {
   throw new PyException(Py.KeyError, "The key does not exit.");
  }
 }
 public boolean __contains__(String key)
 {
  if (data.containsKey(key))
  {
   System.out.println("Found key \"" + key + "\"");
   return true;
  }
  else
  {
   System.out.println("Did not find key \"" + key + "\"");
   return false;
  }
 }
}