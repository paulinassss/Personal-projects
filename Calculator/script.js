let text = document.querySelector('.inp');
let temp = '';
const operators = ['+', '-', '/', '*'];
let res = '';

function number(char)
{

    if (temp.length == 1 && temp == '0' && char != '.')
    {
      return;
    }
    else if (char == '.' && temp != '' && temp[temp.length - 1] == '.')
    {
      return;
    }
    else
    {
      temp += char;
      text.textContent = temp;
    }

}

function oper(char)
{
  if (temp == '' && char == '-')
  {
    temp += char;
    text.textContent = temp;
  }
   else if (temp == '')
   {
     return;
   }
   else
   {
     let op = temp[temp.length-1];
     if (operators.includes(op))
     {
       return;
     }
     else
     {
       temp += char;
       text.textContent = temp;
     }
    }
 }

function allClear()
{
  temp = '';
  text.textContent = '0';
}

function del()s
{
  temp = temp.slice(0, -1);
  if (temp.length == 0)
  {
    text.textContent = '0';
  }
  else
  {
    text.textContent = temp;
  }
}

function result()
{
  res = eval(temp);
  text.textContent = res;
  temp = '';
}
