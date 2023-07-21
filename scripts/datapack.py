from datapackage import Package

package = Package()
#package.get_resource('archive/kazpop.csv')
package.infer('archive/kazpop.csv')
package.infer('data/csv_final.csv')
package.infer('data/rsl1.csv')
#package.infer('archive/source.xlsx')
package.commit()
package.save('datapackage.json')
# package.commit()