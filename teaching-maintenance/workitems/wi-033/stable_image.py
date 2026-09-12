"""Wait for lazy/picture source selection before asking the browser to decode."""
READY='''async i => {
 const until=performance.now()+15000;
 while(performance.now()<until){
   if(i.tagName==='IMG' && i.complete && i.naturalWidth>0){await i.decode();return {src:i.currentSrc,width:i.naturalWidth};}
   if(i.tagName==='OBJECT' && i.contentDocument?.documentElement)return {src:i.data};
   await new Promise(r=>setTimeout(r,50));
 }
 throw Error('Image never loaded: '+(i.currentSrc||i.src||i.data)+' complete='+i.complete+' width='+i.naturalWidth);
}'''
